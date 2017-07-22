import serial
import pyautogui
import re

ser = serial.Serial('COM1',9600,timeout=1)

while True:
  commdata = ser.readline()
  if(commdata):
  	result = re.sub('[^0-9\.]', '', commdata) #filter for number and dot only
  	pyautogui.typewrite(result)
  	pyautogui.press('enter')

