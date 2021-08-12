import cv2 as cv
import numpy as np

from edit_title import EditTitle
from get_pos import GetPos
from get_wrap_height import WrapHeight
from get_wrap_width import WrapWidth
from PIL import ImageFont, ImageDraw, Image

# s = "日本の病棟数に関して民間病院多すぎ問題"
# s2 = "コロナ禍で行われる東京五輪についてどう思う？"
# s3 = "タマホームのワクチン禁止令について"
# s4 = "北海道暑すぎ地球温暖化の影響？"
img = cv.imread("sample/sample_man.png")
title = "コロナ禍で行われる東京五輪についてどう思う？"


class CvPutJaText:  # OpenCVで日本語を表示するためのやつ。
    def __init__(self):
        pass

    @classmethod
    def puttext(cls, cv_image, text, point, font_path, font_size, color=(0, 0, 0)):
        font = ImageFont.truetype(font_path, font_size)

        cv_rgb_image = cv.cvtColor(cv_image, cv.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_rgb_image)

        draw = ImageDraw.Draw(pil_image)
        draw.text(point, text, fill=color, font=font)

        cv_rgb_result_image = np.asarray(pil_image)
        cv_bgr_result_image = cv.cvtColor(
            cv_rgb_result_image, cv.COLOR_RGB2BGR)

        return cv_bgr_result_image


et = EditTitle(title)
edited_title = et.edited_title()

ww = WrapWidth(img)
wrap_width = ww.get_width()

wh = WrapHeight(wrap_width, edited_title)
wrap_height = wh.get_wrap_height()

gp = GetPos(img, title)
get_pos = gp.get_pos()
start_pos = ()
if get_pos == "top_left":
    start_pos = (0, 0)
elif get_pos == "top_right":
    start_pos = (1280-wrap_width, 0)
elif get_pos == "bottom_left":
    start_pos = (0, 720-wrap_height)
elif get_pos == "bottom_right":
    start_pos = (1280-wrap_width, 720-wrap_height)
elif get_pos == "middle_left":
    yohaku_y = int((720 - wrap_height) / 2)
    start_pos = (0, yohaku_y+85)  # ど真ん中だと美しくないので、85ｐｘ下に下げた。
else:  # middle_right
    yohaku_y = int((720 - wrap_height) / 2)
    yohaku_x = 1280 - int(wrap_width * 1.3)
    start_pos = (yohaku_x, yohaku_y+85)


# put gray text wrapper
overlay = img.copy()

x, y, w, h = 10, 10, 10, 10
if (get_pos != "middle_left") and (get_pos != "middle_right"):
    cv.rectangle(overlay, start_pos, (start_pos[0]+wrap_width, start_pos[1]+wrap_height),
                 (0, 0, 0), -1)
else:
    cv.rectangle(overlay, start_pos, (start_pos[0]+int(wrap_width*1.3), start_pos[1]+wrap_height),
                 (0, 0, 0), -1)

alpha = 0.7
img_new = cv.addWeighted(overlay, alpha, img, 1 - alpha, 0)

# put text on wrapper
font_size = wh.px_per_char()
# Macだとフォントの位置がここ。みんなMacだからWindowsは省略する。
font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc"
image = CvPutJaText.puttext(
    img_new, edited_title, start_pos, font_path, font_size, (250, 250, 250))

# download on the Desktop or show image.
cv.imwrite("/Users/morinobuhiro/Desktop/sampleimg.png", image)
# cv.imshow("img", image)
# cv.waitKey()
