from PIL import Image, ImageDraw, ImageFont


font = ImageFont.truetype('Helvetica', 100, encoding="utf-8")

with Image.open('./lgtm/shoebill.jpg', 'r') as im:
    draw_im = ImageDraw.Draw(im)
    width, height = im.size
    draw_im.text((width * 0.5 - 200, height * 0.8), "LGTM", font=font, fill="#000")
    im.save("./lgtm/lgtm.jpg")
