from edit_title import EditTitle
import cv2 as cv
import numpy as np


class WrapHeight:
    def __init__(self, wrap_width, edited_title):
        self.wrap_width = wrap_width
        self.edited_title = edited_title

    def get_max_len(self):
        split_titles = self.edited_title.split('\n')
        max_len = 0
        for title in split_titles:
            if max_len < len(title):
                max_len = len(title)
        return max_len

    def px_per_char(self):
        # middleの部分のフォントサイズがあまりにも小さいので、少し大きくしよう。
        split_by_n = self.edited_title.split('\n')
        original_title = ""
        for seg in split_by_n:
            original_title += seg
        if len(original_title) <= 9:
            return int(self.wrap_width / self.get_max_len() * 1.3)
        return int(self.wrap_width / self.get_max_len())

    def get_gyousuu(self):
        return len(self.edited_title.split('\n'))

    def get_wrap_height(self):
        return self.get_gyousuu() * self.px_per_char()

# img = cv.imread("sample/sample_man.png")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# haar_cascde = cv.CascadeClassifier("sample/haar_face.xml")
# rect = haar_cascde.detectMultiScale(gray)
# for(x, y, w, h) in rect:
#     cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=5)
# cv.imshow("img", img)
# cv.waitKey()
