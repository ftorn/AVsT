import pythoncom, pyHook, sys

def OnKeyboardEvent(event):
    if event.KeyID == 13:
        print "it's showtime"
        sys.exit(0)

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

