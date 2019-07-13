import Pod_Updater
import time

pu = Pod_Updater.Pod_Updater()

time.sleep(2)

pu.get_data()

print pu.data
