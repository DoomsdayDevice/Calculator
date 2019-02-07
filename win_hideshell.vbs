Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c windows.bat"
oShell.Run strArgs, 0, false