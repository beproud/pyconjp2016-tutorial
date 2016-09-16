# read_image.py

from PIL import Image


with Image.open('./2016.png', 'r') as im:
    print('%dx%d' % im.size)
