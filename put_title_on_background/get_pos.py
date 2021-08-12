import cv2 as cv
import numpy as np
import random


class GetPos:
    def __init__(self, img, title):
        self.img = img
        self.title = title

    def is_right(self, rect):

        if type(rect).__module__ == np.__name__:
            (x, y, w, h) = rect[0]
            if(x+w/2 >= 640):
                return True
            else:
                return False
        return False

    def get_pos(self):
        gray = cv.cvtColor(self.img, cv.COLOR_RGB2GRAY)
        # 以下の二行は、該当する場合はnp型で、該当しない場合はからのタプル型を返す。is_rightの場合わけはそれをしている。
        haar_cascade = cv.CascadeClassifier("sample/haar_face.xml")  # 正面
        profile_face = cv.CascadeClassifier("sample/profile_face.xml")  # 横顔
        face_rect1 = haar_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=3)  # 正面
        face_rect2 = profile_face.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=3)  # 横顔

        pos = "left"
        if (self.is_right(face_rect1)) or (self.is_right(face_rect2)):
            pos = "right"

        if(pos == "right"):
            if (len(self.title) <= 9):
                return "middle_left"
            # 60% の確率で、top_left, 四〇％の確率でbottom_leftを返す。
            choice = random.choice([1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
            if choice:
                return "top_left"
            return "bottom_left"
        else:
            if (len(self.title) <= 9):
                return "middle_right"
            # 60% の確率で、top_right, 四〇％の確率でbottom_rightを返す。
            choice = random.choice([1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
            if choice:
                return "top_right"
            return "bottom_right"

# img = cv.imread("sample/sample_man.png")
# insta = GetPos(img, "なぜ我々は？")
# get_pos = insta.get_pos()
# print(get_pos)
