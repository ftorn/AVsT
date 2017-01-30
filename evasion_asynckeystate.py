import sys
from ctypes import *

c = 0
while (c <= 2):
    for i in range(256):
        f = lambda x: x == windll.user32.cdll.user32.GetAsyncKeyState(i) and x in {0x0d}
        c = c + 1
        print c
    sys.stdout.flush()
print "it's showtime.."
