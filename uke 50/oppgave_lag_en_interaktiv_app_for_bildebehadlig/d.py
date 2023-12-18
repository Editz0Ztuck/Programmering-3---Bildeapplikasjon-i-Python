from PIL import Image

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
