import numpy as np
import cv2

def display(w,img):
    cv2.imshow(w, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

canvas =np.zeros((300,300,3),dtype="uint8")
green = (0,255,0)
red = (0,0,255)
#cv2.line(canvas,(0,0),(300,300),green)
#cv2.line(canvas,(0,300),(300,0),red)
#cv2.rectangle(canvas, (10,10),(100,100),green)
cx , cy = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255,255,255)
#for r in range(0,175,25):
    #cv2.circle(canvas,(cx,cy),r,white)
for i in range(0,25):
    radius = np.random.randint(5,200)
    color = np.random.randint(0,256,size=(3,)).tolist()
    pt = np.random.randint(0,300,size=(2,))
    cv2.circle(canvas,tuple(pt),radius,color,-1)awdeawd
display('canvas', canvas)



