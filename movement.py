from typing import List
import sys
import cv2
from djitellopy import tello
import keyPressModule as kp
import time
width = 640
height = 480
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
def getKeyboardInput() -> dict:

    vals_dict = {'lr': 0, 'fb': 0, 'ud': 0, 'yv': 0}
    speed = 100

    if kp.getKey("LEFT"): vals_dict['lr'] = speed
    elif kp.getKey("RIGHT"): vals_dict['lr'] = -speed

    if kp.getKey("UP"): vals_dict['fb'] = speed
    elif kp.getKey("DOWN"): vals_dict['fb'] = -speed

    if kp.getKey("w"): vals_dict['ud'] = speed
    elif kp.getKey("s"): vals_dict['ud'] = -speed

    if kp.getKey("a"): vals_dict['yv'] = speed
    elif kp.getKey("d"): vals_dict['yv'] = -speed

    if kp.getKey("q"): me.takeoff()
    if kp.getKey("e"): me.land()

    return vals_dict

while True:
    frame1 = me.get_frame_read()
    frame2 = frame1.frame
    img = cv2.resize(frame2, (width, height))
    vals = getKeyboardInput()
    me.send_rc_control(vals['lr'], vals['fb'], vals['ud'], vals['yv'])
    if cv2.waitKey(1) == ord('t'):
        break
    cv2.imshow('drone', img)

me.streamoff()
cv2.destroyAllWindows()

