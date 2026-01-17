from PIL import Image
import numpy as np

#Estimated RGB colors
#Romania (lighter blue)
romania_blue = np.array([0, 43, 127])
romania_yellow = np.array([252, 209, 22])
romania_red = np.array([206, 17, 38])

#Chad (darker blue)
chad_blue = np.array([0, 35, 102])
chad_yellow = np.array([254, 203, 0])
chad_red = np.array([198, 12, 48])

#Color processing code
def mean_rgb(img_region):
    return np.array(img_region).mean(axis=(0,1))

def classify_flags(path):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    stripe_width = w // 3

    left = img.crop((0, 0, stripe_width, h))
    middle = img.crop((stripe_width, 0, 2*stripe_width, h))
    right = img.crop((2*stripe_width, 0, w, h))

    left_mean = mean_rgb(left)
    middle_mean = mean_rgb(middle)
    right_mean = mean_rgb(right)

    dist_romania = np.linalg.norm(left_mean - romania_blue) + np.linalg.norm(middle_mean - romania_yellow) + np.linalg.norm(right_mean - romania_red)
    dist_chad = np.linalg.norm(left_mean - chad_blue) + np.linalg.norm(middle_mean - chad_yellow) + np.linalg.norm(right_mean - chad_red)

    return "Romania" if dist_romania < dist_chad else "Chad"

print(classify_flags("C:\LDKCODE\PythonFolder\PythonProject\FlagClassifiers\Romania Chad Flag\Flag_of_Romania.svg.png")) #Replace with your own path
print(classify_flags("C:\LDKCODE\PythonFolder\PythonProject\FlagClassifiers\Romania Chad Flag\Flag_of_Chad.svg.png")) #Replace with your own path