# EF230 base program
# make edits to this code and save as a different filename
# Objective:  drive, turn on LEDS, use OLEDs, get sensor readings

import spheroRVR
import time
# drive forward
spheroRVR.setDriveSpeed(90,90)  # leftwheel, rightwheel, Valid velocity values are [-127..127]
time.sleep(1)
# stop
spheroRVR.setDriveSpeed(0,0)
# spin
spheroRVR.setDriveSpeed(-85,85)
time.sleep(0.1)
# stop
spheroRVR.setDriveSpeed(0,0)
spheroRVR.getDistance
words = ("line1 txt", "line2 txt", "line3 txt")
spheroRVR.setOLED(words) 
time.sleep(3)
