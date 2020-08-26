# python 3.8.5
# -*- coding: utf-8 -*-
import os

import pytesseract
from PIL import Image

path = os.path.split(os.path.realpath(__file__))[0]
image = Image.open(path + '/test.png')
text = pytesseract.image_to_string(image, lang='jpn')

text = text.replace(' ', '')
text = text.replace('\n\n', '\n')
#0
text = text.replace(chr(9450), '0')

#1~20
for num in range(9312,9332):
    text = text.replace(chr(num),str(num - 9311))

print(text)
