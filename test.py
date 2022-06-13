from typing import List
import sys
import cv2
from djitellopy import tello
import keyPressModule as kp
import time
width = 640
height = 480
bbox = (287, 23, 86, 320)
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
i = 0
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
frame1 = me.get_frame_read()
frame2 = frame1.frame
img = cv2.resize(frame2, (width, height))
if __name__ == '__main__':

    tracker0 = ('TLD')
    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker0)

bbox = cv2.selectROI(img, False)
ok = tracker0.init(img, bbox)
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
    ok,frame1 = me.get_frame_read()
    frame2 = frame1.frame
    img = cv2.resize(frame2, (width, height))
    vals = getKeyboardInput()
    me.send_rc_control(vals['lr'], vals['fb'], vals['ud'], vals['yv'])
    #cv2.imshow('drone', img)
    timer = cv2.getTickCount()
    ok, bbox = tracker.update(img)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(img, p1, p2, (255, 0, 0), 2, 1)
    else:
        cv2.putText(img, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv2.putText(img, tracker + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);
    cv2.putText(img, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);
    cv2.imshow("Tracking", img)
    if cv2.waitKey(1) == ord('t'):
        break
    cv2.imshow('drone', img)

me.streamoff()
cv2.destroyAllWindows()