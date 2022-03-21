import cv2 as cv

capture = cv.VideoCapture(0) #Takes integer arguments for connected webcam(s) or a path to a video. 0 = webcam

while True:
    isTrue, frame = capture.read()
    
    cat_haar_cascade = cv.CascadeClassifier(r'C:\Users\JHolt\OneDrive\Documents\Projects\Engineering\Kitty_Cannon\GUI_Files\haarcascade_frontalcatface.xml')
    human_haar_cascade = cv.CascadeClassifier(r'C:\Users\JHolt\OneDrive\Documents\Projects\Engineering\Kitty_Cannon\GUI_Files\haar_face.xml')
    #By increasing the minimum neighbors parameter, it will be less sensitive to noise
    cat_faces_rect = cat_haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors = 100)
    human_faces_rect = human_haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors = 6)
    #still getting false positives with my nose and mouth (this will make for some funny accidents)
    #In the notes for the cat haar cascade, it is recommended to use both a human and cat face detector. If they overlap, reject it

    for (x2,y2,w2,h2) in human_faces_rect:
        cv.rectangle(frame, (x2,y2), (x2+w2,y2+h2), (0,255,0), thickness=2)
    
    for (x,y,w,h) in cat_faces_rect:
        if x > x2 and x+w < x2+w2 and y > y2 and y+h < y2+h2:
            continue
        else:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), thickness=2)
    
    cv.imshow('Video', frame)


    if cv.waitKey(20) & 0xFF==ord('d'): #if the d key is pressed
        break

capture.release()
cv.destroyAllWindows()