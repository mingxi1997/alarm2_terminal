import os
import time

count=0
while True:
    if count>1440:
        os.system('reboot')
    time.sleep(60)
    count+=1
