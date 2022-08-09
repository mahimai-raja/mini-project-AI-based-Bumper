import cv2
from func import *


video = cv2.VideoCapture('live_road.mp4')

while True :
    return_val, frame = video.read() 
    out = process_image(frame)
    Lane = cv2.addWeighted(frame,0.8,out,1.,0.)
    cv2.imshow('Lane Detection',Lane)

    if cv2.waitKey(2) % 256 == 27:  
        break
    
video.release()
cv2.destroyAllWindows()
