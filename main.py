import subprocess
import time
import pandas as pd
from datetime import datetime
import webbrowser
import keyboard
import AVFoundation as AVF
import Quartz
import objc
from Foundation import NSObject, NSURL
import os
from pyautogui import press, typewrite, hotkey
from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps

#from selenium import webdriver

# Reading the file
df = pd.read_csv('Lectures.csv')
print("Program Started !")
print(datetime.now().strftime("%d-%m-%Y-%H-%M"))


while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%a %H:%M")
    now1 = datetime.now().strftime("%a %H:%M")
    display_id = Quartz.CGMainDisplayID()
    session = AVF.AVCaptureSession.alloc().init()
    devices = AVF.AVCaptureDevice.defaultDeviceWithMediaType_(AVF.AVMediaTypeAudio)
    screen_input = AVF.AVCaptureScreenInput.alloc().initWithDisplayID_(display_id)
    error = None
    audio, error = AVF.AVCaptureDeviceInput.deviceInputWithDevice_error_(devices, objc.nil)
    file_output = AVF.AVCaptureMovieFileOutput.alloc().init()
    session.addInput_(screen_input)
    session.addInput_(audio)
    session.addOutput_(file_output)
    if now in str(df['starttime']):
       row = df.loc[df['starttime'] == now]
       link = str(row.iloc[0,1])
       pwd = str(row.iloc[0,3])
       if link.startswith('http'):
        if pd.isnull(df.loc[0, 'pass']):
          now = datetime.now()
          dt_file_name = now.strftime("ZoomRecording-%Y-%m-%d_%H-%M-%S.mov")
          session.startRunning()
          file_url = NSURL.fileURLWithPath_(dt_file_name)
          file_url = file_output.startRecordingToOutputFileURL_recordingDelegate_(file_url, NSObject.alloc().init())
          webbrowser.open(link)
          print("1")
          time.sleep(10)       
          time.sleep(60)
        else:
          now = datetime.now()
          dt_file_name = now.strftime("ZoomRecording-%Y-%m-%d_%H-%M-%S.mov")
          session.startRunning()
          file_url = NSURL.fileURLWithPath_(dt_file_name)
          file_url = file_output.startRecordingToOutputFileURL_recordingDelegate_(file_url, NSObject.alloc().init())
          webbrowser.open(link)
          print("2")
          time.sleep(15)
          typewrite(pwd, interval=0.4)
          time.sleep(10)
          press('enter')
          time.sleep(10)      
          time.sleep(60)

       else:
       	now = datetime.now()
       	dt_file_name = now.strftime("ZoomRecording-%Y-%m-%d_%H-%M-%S.mov")
       	session.startRunning()
        file_url = NSURL.fileURLWithPath_(dt_file_name)
        file_url = file_output.startRecordingToOutputFileURL_recordingDelegate_(file_url, NSObject.alloc().init())
       	
        # driver = webdriver.Chrome("bin/chromedriver")
        link1 = "https://zoom.us/join"
        # print("3")
        # chrome=subprocess.Popen(["bin/Chromium.app/Contents/MacOS/Chromium", link1], shell = True, stdout=subprocess.PIPE)
       	webbrowser.open(link1)
        time.sleep(15)
       	typewrite(link, interval=0.4)
       	time.sleep(10)
       	press('enter')
        time.sleep(10)
       	typewrite(pwd, interval=0.4)
       	time.sleep(10)
       	press('enter')
       	time.sleep(60)
       	
    if now1 in str(df['endtime']):
        session.stopRunning()
        keyboard.press_and_release('command+q')
        print("end")
        time.sleep(60)     

        
