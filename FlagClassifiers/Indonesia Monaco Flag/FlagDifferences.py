from PIL import Image
import numpy as np

#Estimated aspect ratios

#Indonesia:
indonesia_aspect_ratio = 2/3

#Monaco:
monaco_aspect_ratio = 4/5

#Aspect ratio processing code
def classify_flags(path):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    aspect_ratio = h/w
    dist_indonesia = abs(aspect_ratio - indonesia_aspect_ratio)
    dist_monaco = abs(aspect_ratio - monaco_aspect_ratio)
    return "Indonesia" if dist_indonesia < dist_monaco else "Monaco"
print(classify_flags("C:\LDKCODE\PythonFolder\PythonProject\FlagClassifiers\Indonesia Monaco Flag\Flag_of_Indonesia.svg.webp"))
print(classify_flags("C:\LDKCODE\PythonFolder\PythonProject\FlagClassifiers\Indonesia Monaco Flag\Flag_of_Monaco.svg.png"))