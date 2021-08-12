import cv2 as cv
import numpy as np
import face_recognition


class WrapWidth:
    def __init__(self, img):
        self.img = img

    def get_rect(self):
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        haar_cascade = cv.CascadeClassifier("sample/haar_face.xml")
#        profile_cascade = cv.CascadeClassifier("sample/profile_face.xml")
        rect1 = haar_cascade.detectMultiScale(gray)
 #       rect2 = profile_cascade.detectMultiScale(
#            gray, scaleFactor=1.1, minNeighbors=3)
        rect2 = face_recognition.face_locations(
            self.img, number_of_times_to_upsample=1, model='hog')
        if type(rect1).__module__ == np.__name__:
            return rect1

        return rect2

    def get_width(self):
        rect = self.get_rect()
        print(rect)
        (x, y, w, h) = rect[0]
        return max(x, 1280-x-w)
