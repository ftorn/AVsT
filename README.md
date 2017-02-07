AVsT (AntiVirus Evasion simple Trick)
=====================================

## Evasion through asynckeystate 

- Do you want to bypass the AV software? You can use GetAsyncKeyState function and wait until a user types some special keys 
  - windows only version
  - in the example I check the state of RETURN key
- to execute
  - python evasion_asynckeystate.py

## Evasion through hook key 
  - windows only version
  - in the example I check the state of RETURN key
- to execute
  - python evasion_hookkey.py

## Evasion through thickcount
- AVs normaly bypass the sleep function so you can use the GetThickCount() [From MSDN: Retrieves the number of milliseconds that have elapsed since the system was started, up to 49.7 days]
  - windows only version
  - in the example I set 10 sec
- to execute
  - python evasion_thickcount.py
