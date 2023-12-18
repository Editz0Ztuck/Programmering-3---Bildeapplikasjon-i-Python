from PIL import Image
import pilgram

im = Image.open('bilder/chicken.jpg')
pilgram.moon(im).save('sample-moon.jpg')