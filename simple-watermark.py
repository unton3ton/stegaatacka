from PIL import Image

filename = 're2.png'
watermark = Image.open(filename, 'r')
filename1 = 'tinne-7.jpeg'
bg = Image.open(filename1, 'r')
width, height = bg.size
k = 0.25
newsize = (int(k*width), int(k*height))
watermark = watermark.resize(newsize)
text_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
text_img.paste(bg, (0,0))
text_img.paste(watermark, (0,0), mask=watermark)
text_img.save("simple-result.png", format="png")