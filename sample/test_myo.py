import sys
import time
import RPi.GPIO as GPIO
sys.path.append('../lib/')
M1F=16
M1R=20
M2F=19
M2R=26


GPIO.setmode(GPIO.BCM)                        
GPIO.setwarnings(False)
GPIO.setup(M1F,GPIO.OUT)
GPIO.setup(M2F,GPIO.OUT)
GPIO.setup(M1R,GPIO.OUT)
GPIO.setup(M2R,GPIO.OUT)

from myo import Myo
from print_pose_listener import PrintPoseListener
from vibration_type import VibrationType
from pose_type import PoseType
from device_listener import DeviceListener




def main():
    print('Start Myo for Linux')

    listener = PrintPoseListener()
    myo = Myo()

    try:
        myo.connect()
        myo.add_listener(listener)
        myo.vibrate(VibrationType.SHORT)
        while True:
            myo.run()

    except KeyboardInterrupt:
        pass
    except ValueError as ex:
        print(ex)
    finally:
        myo.safely_disconnect()
        print('Finished.')

if __name__ == '__main__':
    main()
    
    
    
