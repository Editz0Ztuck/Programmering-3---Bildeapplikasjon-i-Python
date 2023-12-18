from PIL import Image
import os

Original_Image = Image.open(r'C:\Users\marce\OneDrive - Viken fylkeskommune\Desktop\uke 50\bilder\chicken.jpg')

def image_rotator(rotate):
    rotated_image1 = Original_Image.rotate(rotate)
    rotated_image1.save('rotated_chicken.jpg') 
    os.startfile('rotated_chicken.jpg')
    
print("type how much you want to rotate the image")

rotate = int(input("choose here:   "))
image_rotator(rotate)