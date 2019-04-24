import sys
import time
import RPi.GPIO as GPIO
M1F=16
M1R=20
M2F=19
M2R=26

sys.path.append('../lib/')

GPIO.setmode(GPIO.BCM)                        
GPIO.setwarnings(False)
GPIO.setup(M1F,GPIO.OUT)
GPIO.setup(M2F,GPIO.OUT)
GPIO.setup(M1R,GPIO.OUT)
GPIO.setup(M2R,GPIO.OUT)


from device_listener import DeviceListener
from pose_type import PoseType

class PrintPoseListener(DeviceListener):
	def on_pose(self, pose):
            pose_type = PoseType(pose)
            print(pose_type.name)
            if ( pose_type.name== "FINGERS_SPREAD"):
                #forward
                GPIO.output(M1F,1)
                GPIO.output(M2F,1)
                GPIO.output(M1R,0)
                GPIO.output(M2R,0)
            elif(pose_type.name== "DOUBLE_TAP"):
                #reverse
                GPIO.output(M1F,0)
                GPIO.output(M2F,0)
                GPIO.output(M1R,1)
                GPIO.output(M2R,1)
            elif(pose_type.name== "WAVE_IN"):
                #left
                GPIO.output(M1F,0)
                GPIO.output(M2F,1)
                GPIO.output(M1R,0)
                GPIO.output(M2R,0)
            elif(pose_type.name== "WAVE_OUT"):
                #right
                GPIO.output(M1F,1)
                GPIO.output(M2F,0)
                GPIO.output(M1R,0)
                GPIO.output(M2R,0)
            elif(pose_type.name== "FIST"):
                #stop
                GPIO.output(M1F,0)
                GPIO.output(M2F,0)
                GPIO.output(M1R,0)
                GPIO.output(M2R,0)
                
                
                 
                 
                    
