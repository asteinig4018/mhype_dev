#!/usr/bin/env python3

import asyncio
import websockets
import socket
from concurrent.futures import ThreadPoolExecutor
import Incoming_Message_Handler
import Transmitter

#############################################
'''
app

This runs the recieving server for the base station and forwards
messages on to pod.js

This file is written for Python 3 unlike the other files in this folder
'''
############################################

class Base_Server:

    #####   UDP HANDLING   #####
    def __init__(self):
        self.UDP_HOST = "127.0.0.1"
        self.UDP_PORT = 3000
        self.BUFFER_SIZE = 1024

        self.imh = Incoming_Message_Handler.Incoming_Message_Handler()
        self.transmitter = Transmitter.Transmitter()

    async def consumer(self, msg, sock):
        #convert to json
        data = {} #+msg
        data['active_count']:self.transmitter.get_count()
        # Sends message from websocket to pod
        self.transmitter.send_message(data)
        
        #sock.sendto(bytearray(msg, "utf-8"), (self.UDP_HOST, self.UDP_PORT))

    async def consumer_handler(self, websocket, sock, path):
        while True:
            # Waits for message from websocket (future use: buttons)
            message = await websocket.recv()
            await consumer(message, sock)

    async def producer(self, sock):
        try:
            sock.sendto(bytearray("poll", "utf-8"), (self.UDP_HOST, self.UDP_PORT))
            loop = asyncio.get_event_loop()

            # Data is received from the pod
            data, addr = await loop.run_in_executor(None, sock.recvfrom, self.BUFFER_SIZE)
            await asyncio.sleep(0.5)
            print('data=', data)
            print('addr=', addr)

            # Data changed here to say that the pod is connected
            # data = '{ "type": "pod_message", "body": "ok" }'
            data = '{ "type": "velocity_change", "body": ' + str(int(data)) + ' }'

        except socket.timeout:
            data = '{ "type": "pod_error", "body": "disconnected" }'
            print("timeout")

        return data

    async def producer_handler(self, websocket, sock, path):
        print("started producer")
        while True:
            msg = await self.producer(sock)

            #checks if message should be passed on
            message = self.imh.handle_message(msg)

            #filters counter updates and error messages
            if message != None and message:

            #if msg != "":
                # Sends msg (data returned from producer) to websocket 
                # This looks like it's being received in app/src/js/store/reducers/pod.js
                # Also looks like app/src/js/store/actions/types.js is something
                # Also app/src/js/state/index.js
                await websocket.send(msg)

    # Async stuff
    async def handler(self, ws, path):
        print("started socket")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.settimeout(0.5)

        consumer_task = asyncio.ensure_future(consumer_handler(ws, sock, path))
        producer_task = asyncio.ensure_future(producer_handler(ws, sock, path))

        done, pending = await asyncio.wait([consumer_task, producer_task], return_when=asyncio.FIRST_COMPLETED)

        for task in pending:
            task.cancel()

    #####   MAIN CODE   #####
    def run(self):

        server = websockets.serve(self.handler, 'localhost', 8000)

        print("started websocket connection at localhost:8000")

        loop = asyncio.get_event_loop()

        loop.run_until_complete(server)
        loop.run_forever()


#main
base_server = Base_Server()
base_server.run()