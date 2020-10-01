Set Shell = CreateObject("WScript.Shell")
DesktopPath = Shell.SpecialFolders("Desktop")
Set link = Shell.CreateShortcut(DesktopPath & "\F.R.I.D.A.Y.lnk")
link.Arguments = "1 2 3"
link.Description = "test shortcut"
link.HotKey = "CTRL+ALT+SHIFT+X"
link.IconLocation = "C:\Program Files\F.R.I.D.A.Y\F.R.I.D.A.Y.ICO"
link.TargetPath = "C:\Program Files\F.R.I.D.A.Y\F.R.I.D.A.Y.exe"
link.WindowStyle = 3
link.WorkingDirectory = "C:\Program Files\F.R.I.D.A.Y"
link.Save