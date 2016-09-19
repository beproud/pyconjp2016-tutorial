from PIL import Image


with Image.open('./2016.png', 'r') as im:
    im.save('./2016.jpg', 'JPEG')
