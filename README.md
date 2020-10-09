#macOSAutoJoinAndRecordZoomSession

This tool can be used to automatically Join Zoom Sessions and Record the desktop. It uses pandas to read the start time, end time, weekday, zoom id or link and password stored inside a csv file. The csv file can be edited with the csvreader.py or manually with text editor. The screen is recorded with pyobjc-Framework-avfoundation.

To record the desktop audio you need to install kernel extension.

https://download.vb-audio.com/Download_MAC/VBCable_MACDriver_Pack107.dmg

And you need to do this steps shown in the pictures bellow:

Command + Space = > Spotlight search 

![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi.png?raw=true)
![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi1.png?raw=true)
![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi2.png?raw=true)
![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi3.png?raw=true)
![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi4.png?raw=true)
![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi5.png?raw=true)
![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi6.png?raw=true)
![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi7.png?raw=true)
![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/midi8.png?raw=true)


zoom settings

![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/ZoomSettings.png?raw=true)



![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/ZoomSettings1.png?raw=true)

When the endtime is the current time in the terminal window you will be promted to terminate the process. If you want to continue running the process click Cancel

![alt text](https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession/blob/main/terminal.png?raw=true)

You need Google Chrome or any chromium based browser

If there is an error install pyhton 3 and create virtual environment and install the following packages 


pip install -r requirements.txt
