# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw

img = Image.open('C:/Users/meyl-/Downloads/ChatGPT Image 2026年6月8日 22_35_50.png').copy()
draw = ImageDraw.Draw(img)

characters = [
    # 100%
    ("ISFJ",  (250, 160, 680, 420)),

    # 80%
    ("INFJ",  (140, 450, 440, 670)),
    ("ESFJ",  (440, 450, 730, 670)),
    ("ISTJ",  (730, 450, 1010, 670)),

    # 50%上段
    ("ENFJ",  (140, 700, 365, 920)),
    ("ESTP",  (365, 700, 590, 920)),
    ("ESFP",  (590, 700, 805, 920)),
    ("ENFP",  (805, 700, 1010, 920)),

    # 50%下段
    ("INFP",  (140, 940, 365, 1160)),
    ("ISFP",  (365, 940, 590, 1160)),
    ("INTP",  (590, 940, 805, 1160)),
    ("INTJ",  (805, 940, 1010, 1160)),

    # 20%
    ("ENTJ",  (140, 1210, 365, 1490)),
    ("ENTP",  (365, 1210, 590, 1490)),
    ("ISTP",  (590, 1210, 805, 1490)),
    ("ESTJ",  (805, 1210, 1010, 1490)),
]

for name, box in characters:
    draw.rectangle(box, outline="red", width=3)

img.save('C:/Users/meyl-/Downloads/check_boxes.png')
print("check_boxes.png を保存したよ！")
