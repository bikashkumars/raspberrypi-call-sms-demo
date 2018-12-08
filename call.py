import serial
import RPi.GPIO as GPIO      
import os, time

GPIO.setmode(GPIO.BOARD)    

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)


#Call a number and check for status
networkData = ""
port.write('ATD9861098610+'+';\r')      # Disable the Echo
time.sleep(3)
networkData = port.read(30)
print networkData
status = networkData.find("OK")
if status >=0:
	print "Calling"
else:
	print "Call might fail"

