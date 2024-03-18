
import cv2 as cv
import deutsch_autobahn.rescale as scale

'reading image'
#img = cv.imread('C:/Users/danny/openCV/photo/test.png')
#cv.imshow("CAT",img)
#cv.waitKey()

'reading video'
capture = cv.VideoCapture('C:/Users/danny/openCV/deutsch_autobahn/autobahn.mp4')

'while loop to read vidoe frame by fram '
while True:
    'read the image frame by frame and return boolean whether read or not'
    isTrue, frame,  = capture.read() 

    'display each individual frame'
   # frame = scale.rescaleFrame(frame)
    cv.imshow('video',frame)

    'Press (d) key to exit'     
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

'we releas all capture point and close all windows'
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)