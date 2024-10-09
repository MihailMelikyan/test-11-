from PIL import Image

im = Image.open('cat.jpg')
print(im.format,im.size,im.mode)

im.show()

