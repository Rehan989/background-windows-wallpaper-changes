# background-windows-wallpaper-changes

#Program for changing the desktop wallpaper at every defined amount of seconds in conf.json

For running the script on startup
1. open the changeWallpaper.ps1 file and edit the file directories as required and paste it to the desktop for running the file
2. Open windows run using windows key + R key and type shell:startup and create a file startup.cmd
Paste the following commands in the startup.cmd file:
PowerShell -Command "Set-ExecutionPolicy Unrestricted" >> "%TEMP%\StartupLog.txt" 2>&1
PowerShell C:\Users\%user%\Desktop\script.ps1 >> "%TEMP%\StartupLog.txt" 2>&1

After proper configuration your code can works

# Thank you
