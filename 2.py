from PIL import Image


RATIO = 0.5

with Image.open('./2016.png', 'r') as im:
    width, height = im.size
    resized = im.resize((
        int(RATIO * width),
        int(RATIO * height),
    ))
    resized.save('./resized-2016.png')
