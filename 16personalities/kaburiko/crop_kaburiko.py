from PIL import Image
import os

img = Image.open('C:/Users/meyl-/Downloads/ChatGPT Image 2026年6月8日 22_35_50.png')
w, h = img.size  # 1024 x 1536

output_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(output_dir, exist_ok=True)

# (left, upper, right, lower) で切り抜き
characters = [
    # かぶりこ度100%
    ("ISFJ_真の純情かぶりこちゃん",   (210, 110, 620, 370)),

    # かぶりこ度80%
    ("INFJ_お察しかぶりこちゃん",     (45,  385, 355, 620)),
    ("ESFJ_お世話やきかぶりこちゃん", (355, 385, 665, 620)),
    ("ISTJ_しっかりかぶりこちゃん",   (665, 385, 995, 620)),

    # かぶりこ度50% 上段
    ("ENFJ_にこにこリーダーかぶりこ", (45,  640, 295, 870)),
    ("ESTP_おてんばかぶりこ",         (295, 640, 545, 870)),
    ("ESFP_おまつりかぶりこ",         (545, 640, 790, 870)),
    ("ENFP_ゆめみるかぶりこ",         (760, 640, 1000, 870)),

    # かぶりこ度50% 下段
    ("INFP_ロマンチストかぶりこ",     (45,  875, 295, 1110)),
    ("ISFP_アーティストかぶりこ",     (295, 875, 545, 1110)),
    ("INTP_ひきこもり学者かぶりこ",   (545, 875, 790, 1110)),
    ("INTJ_一匹狼かぶりこ",           (760, 875, 1000, 1110)),

    # かぶりこ度20%
    ("ENTJ_プレジデントかぶりこ",     (45,  1155, 295, 1430)),
    ("ENTP_へりくつかぶりこ",         (295, 1155, 545, 1430)),
    ("ISTP_職人肌かぶりこ",           (545, 1155, 790, 1430)),
    ("ESTJ_熱血キャプテンかぶりこ",   (760, 1155, 1000, 1430)),
]

for name, box in characters:
    cropped = img.crop(box)
    filepath = os.path.join(output_dir, f"{name}.png")
    cropped.save(filepath)
    print(f"保存: {name}.png")

print("完了！")
