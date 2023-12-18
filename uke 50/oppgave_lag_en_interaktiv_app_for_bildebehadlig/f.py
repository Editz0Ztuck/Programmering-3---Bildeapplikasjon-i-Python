from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

drugs = input("text: ")


filepath = os.path.join(os.path.dirname(__file__), "chicken.jpg")

img = Image.open(filepath)
draw = ImageDraw.Draw(img)
don_size = 30
font = ImageFont.load_default().font_variant(size=don_size)

draw.text((10, 19), drugs, fill=(255, 0, 0), font=font)

img.save("YES2.png")