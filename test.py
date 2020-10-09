import time
import AVFoundation as AVF
import Quartz
import objc

from Foundation import NSObject, NSURL

def main():
    display_id = Quartz.CGMainDisplayID()

    session = AVF.AVCaptureSession.alloc().init()
    devices = AVF.AVCaptureDevice.defaultDeviceWithMediaType_(AVF.AVMediaTypeAudio)
    print(devices)
    screen_input = AVF.AVCaptureScreenInput.alloc().initWithDisplayID_(display_id)
    error = None
    audio, error = AVF.AVCaptureDeviceInput.deviceInputWithDevice_error_(devices, objc.nil)
    file_output = AVF.AVCaptureMovieFileOutput.alloc().init()

    session.addInput_(screen_input)
    session.addInput_(audio)
    session.addOutput_(file_output)
    session.startRunning()

    file_url = NSURL.fileURLWithPath_('fooste.mov')
    # Cheat and pass a dummy delegate object where normally we'd have a
    # AVCaptureFileOutputRecordingDelegate
    file_url = file_output.startRecordingToOutputFileURL_recordingDelegate_(
                file_url, NSObject.alloc().init())
    time.sleep(30)
    session.stopRunning()

if __name__ == '__main__':
    main()
