import win32api, time

start = int(win32api.GetTickCount())
time.sleep(10)
total = ((int(win32api.GetTickCount()) - start) / 1000 )
f = lambda x: x <= 10 and "AV == NO" or "AV == YES"
print f(total)
