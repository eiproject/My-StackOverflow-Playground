from PIL import Image

imgg = Image.open('image.png')
imgg.thumbnail((400, 400))
imgg.save('thumbnail_400.tif')