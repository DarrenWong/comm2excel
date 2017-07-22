# comm2excel

Transfer some devices input data to the PC's excel file by COMM or RS232 port for record propose. This one might help.

Installation
------------
Need to install Python 2 or 3. And two modules using pip
```Shell
$ pip install pyserial
$ pip install pyautogui
```

Changed the comm config('COMX',9600 or /dev/ttyX) in the python below that matching your real device:

```Python
ser = serial.Serial('COMX',9600,timeout=1)
```

Then start and try it.
