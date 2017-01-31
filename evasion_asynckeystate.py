import sys
from ctypes import *
user32   = windll.user32
GetAsyncKeyState = cdll.user32.GetAsyncKeyState

c = 0
while (c <= 2):
    for i in range(256):
        if user32.GetAsyncKeyState(i) & True:
            if i in {0x0d}:
                c = c + 1
                print c
print "it's showtime"
