from PIL import Image

padding = 32
opacity = 127
img = Image.open("image.png").convert('RGBA')

x, y, w, h = padding, padding, img.width - padding, img.height - padding
img_cropped = img.crop((x, y, w, h))

img.putalpha(127)

img.paste(img_cropped, (x, y))
img.save('image_new.png')