import cv2
from collections import deque
from numpy import mean

face_samples = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
frameHeights = deque(maxlen=50)
frameWidths = deque(maxlen=50)

while True:  
    _, img = cap.read()  
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_samples.detectMultiScale(gray_img, 1.25, 4) 
  
    for (x,y,w,h) in faces:
        frameHeights.append(h)
        frameWidths.append(w)
        cv2.rectangle(img,
                      (x,y),
                      (x+w,y+h),
                      (255,255,0),
                      2)  
        cv2.putText(img,
                    f"Width: {mean(frameWidths):.1f}, Height: {mean(frameHeights):.1f}",
                    (0,30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,0),
                    1,
                    2
                    )
        
    cv2.imshow('Face Recognition',img) 
  
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
cap.release() 
cv2.destroyAllWindows()