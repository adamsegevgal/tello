import numpy as np
import cv2
import time
from djitellopy import Tello
width = 640
height = 480
me = Tello()
me.connect()
me.streamon()
cap = cv2.VideoCapture(0)


fps = 0
while True:
    start_time = time.time()
   # ret, frame = cap.read()
    frame1 = me.get_frame_read()
    frame2 = frame1.frame
    img = cv2.resize(frame2,(width,height))
    #print(frame.shape)
    #cv2.putText(frame,'FPS:{:.0f}'.format(fps),(30,60),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),1)
   # cv2.putText(img, 'FPS:{:.0f}'.format(fps),(30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 1)
    #hstack = np.hstack((frame,img))
    #cv2.imshow('camera',frame)
    cv2.imshow('drone', img)
   # cv2.imshow('camerat', hstack)
    if cv2.waitKey(1) == ord('q'):
        break
    time_taken = time.time()-start_time
    fps = 1/time_taken
me.streamoff()
cap.release()
cv2.destroyAllWindows()
