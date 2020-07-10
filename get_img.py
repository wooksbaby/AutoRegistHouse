from PIL import Image, ImageDraw, ImageFont
import random
import glob
import numpy as np
import pandas as pd
import pyautogui


def get_an_image(owner_name):  # get an image

    font = random.choice(glob.glob('font\*.ttf'))
    font2 = random.choice(glob.glob('font\*.ttf'))
    font3 = random.choice(glob.glob('font\*.ttf'))

    while font == font2:
        font = random.choice(glob.glob('font\*.ttf'))
        font2 = random.choice(glob.glob('font\*.ttf'))

    check_box = Image.new("RGBA", (25, 25), (255, 255, 255, 255))
    check_box.save("temp_check.png")

    base = Image.new("RGBA", (175, 50), (255, 255, 255, 255))
    base.save("temp.png")

    base2 = Image.new("RGBA", (175, 50), (255, 255, 255, 255))
    base2.save("temp2.png")

    # make a blank image for the text, initialized to transparent text color
    check_box_v = Image.new("RGBA", check_box.size, (0, 0, 0, 255))
    txt = Image.new("RGBA", base.size, (0, 0, 0, 255))
    txt2 = Image.new("RGBA", base2.size, (0, 0, 0, 255))
    # get a font

    fnt_check = ImageFont.truetype(str(font3), random.randrange(30, 31))  # 체크박스
    fnt = ImageFont.truetype(str(font), random.randrange(43, 45))  # 성명
    fnt_sign = ImageFont.truetype(str(font2), random.randrange(50, 51))  # 싸인

    # get a drawing context

    check = ImageDraw.Draw(check_box_v)
    name = ImageDraw.Draw(txt)
    sign = ImageDraw.Draw(txt2)
    # draw text, full opacity

    check_box_x = random.randrange(5, 7)
    check_box_y = random.randrange(-10, -5)

    start_x = random.randrange(20, 30)
    start_y = random.randrange(-4, -1)

    start_sign_x = random.randrange(30, 40)
    start_sign_y = random.randrange(-4, -1)

    check.text((check_box_x, check_box_y), 'V', font=fnt_check, fill=(255, 255, 255, 255))
    name.text((start_x, start_y), owner_name[0]+' '+owner_name[1:], font=fnt, fill=(255, 255, 255, 255))
    sign.text((start_sign_x, start_sign_y), owner_name[0], font=fnt_sign, fill=(255, 255, 255, 255))

    outv = Image.alpha_composite(check_box, check_box_v)
    out1 = Image.alpha_composite(base, txt)
    out2 = Image.alpha_composite(base2, txt2)

    outv.save('out0.png')
    out1.save('out1.png')
    out2.save('out2.png')



