import cv2
import sys, os
import math

def detect_faces():
    path = os.path.dirname(os.path.realpath(__file__))
    #print(path)
    faceCascade = cv2.CascadeClassifier(path+"/data/haarcascade_frontalface_default.xml")

    video_capture = cv2.VideoCapture(0)

    faces_number = 0

    frames = 5

    while frames > 0:

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        faces_number = len(faces)
        #print(faces_number)


        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        frames = frames - 1



    # Display the resulting frame
    #cv2.imshow('Video', frame)

    cv2.imwrite(path+"/data/faces.jpg",frame)

    print(str(faces_number) + " faces detected.")

    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

    return faces_number

#detect_faces()
