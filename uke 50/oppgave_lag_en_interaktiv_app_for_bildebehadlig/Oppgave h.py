from PIL import Image
import pilgram
import os


def opg1and2():

    im = Image.open('bilder/chicken.jpg')
    pilgram.moon(im).save('sample-moon.jpg')

def opg3():
    
    Original_Image = Image.open(r'C:\Users\marce\OneDrive - Viken fylkeskommune\Desktop\uke 50\bilder\chicken.jpg')

    def image_rotator(rotate):
        rotated_image1 = Original_Image.rotate(rotate)
        rotated_image1.save('rotated_chicken.jpg') 
        os.startfile('rotated_chicken.jpg')
        
    print("type how much you want to rotate the image")

    rotate = int(input("choose here:   "))
    image_rotator(rotate)

def opg4():

    original_image = Image.open(r'C:\Users\marce\OneDrive - Viken fylkeskommune\Desktop\uke 50\bilder\chicken.jpg')

    bredde, høyde = original_image.size #henter høyde på det eksisterende bilde
    ønsket_bredde = 1080

    # Beregn proporsjonal høyde basert på ønsket bredde
    ønsket_høyde = int((høyde / bredde) * ønsket_bredde)

    # Sjekk om bildet allerede har minimumsbredde
    if bredde >= ønsket_bredde:
        endret_bilde = original_image.copy()
    else:
        endret_bilde = original_image.resize((ønsket_bredde, ønsket_høyde))

    endret_bilde.save('endret_bilde.jpg')

def opg5():
    drugs = input("text: ")

    filepath = os.path.join(os.path.dirname(__file__), "chicken.jpg")

    img = Image.open(filepath)
    draw = ImageDraw.Draw(img)
    don_size = 30
    font = ImageFont.load_default().font_variant(size=don_size)

    draw.text((10, 19), drugs, fill=(255, 0, 0), font=font)

    img.save("YES2.png")

def opg6():
    def add_polaroid_frame(image_path, frame_path, output_path):
 
        image = Image.open(image_path)
        frame = Image.open(frame_path)
    
        width, height = image.size
        min_dimension = min(width, height)
        cropped_image = image.crop(((width - min_dimension) // 2, (height - min_dimension) // 2,
                                    (width + min_dimension) // 2, (height + min_dimension) // 2))
    
        scaled_image = cropped_image.resize((760, 760), Image.LANCZOS)
    
        canvas = Image.new('RGB', frame.size)
        canvas.paste(scaled_image, (64, 64))
    
        canvas.paste(frame, (0, 0), frame)  
    
        canvas.save(output_path)
        
        image_path = 'bilder/chickenc.png'
        frame_path = 'bilder/polaroid.png'
        output_path = 'saved photo polaroid.jpg'
        
        add_polaroid_frame(image_path, frame_path, output_path)


print(" now you will get 5 choices, choose 1-5")

print("1: instagram filter")
print("2: rotate image")
print("3: klipper bide")
print("4: leg til text til bilde")
print("5: polaroid frame til bildet")

da_choice = input("velg her 1-5: ")

if da_choice == '1':
    opg1and2()

elif da_choice == '2':
    opg3()

elif da_choice == '3':
    opg4()

elif da_choice == '4':
    opg5()

elif da_choice == '5':
    opg6()
