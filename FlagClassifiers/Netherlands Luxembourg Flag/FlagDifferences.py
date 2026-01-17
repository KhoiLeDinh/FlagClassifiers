from PIL import Image
import numpy as np
#Estimated RGB colors

#Netherlands:
netherlands_red = np.array([174, 28, 40])
netherlands_white = np.array([255, 255, 255])
netherlands_blue = np.array([33, 70, 139])

#Luxembourg:
luxembourg_red = np.array([206, 17, 38])
luxembourg_white = np.array([255, 255, 255])
luxembourg_blue = np.array([0, 51, 160])

#Color processing code
def mean_rgb(img_region):
    return np.array(img_region).mean(axis=(0,1))
def classify_flags(path):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    stripe_height = h // 3
    top = img.crop((0, 0, w, stripe_height))
    middle = img.crop((0, stripe_height, w, 2*stripe_height))
    bottom = img.crop((0, 2*stripe_height, w, h))
    top_mean = mean_rgb(top)
    middle_mean = mean_rgb(middle)
    bottom_mean = mean_rgb(bottom)
    dist_netherlands = np.linalg.norm(top_mean - netherlands_red) + np.linalg.norm(middle_mean - netherlands_white) + np.linalg.norm(bottom_mean - netherlands_blue)
    dist_luxembourg = np.linalg.norm(top_mean - luxembourg_red) + np.linalg.norm(middle_mean - luxembourg_white) + np.linalg.norm(bottom_mean - luxembourg_blue)
    return "Netherlands" if dist_netherlands < dist_luxembourg else "Luxembourg"
print(classify_flags("C:\\LDKCODE\\PythonFolder\\PythonProject\\FlagClassifiers\\Netherlands Luxembourg Flag\\Flag_of_the_Netherlands.svg.webp"))
print(classify_flags("C:\\LDKCODE\\PythonFolder\\PythonProject\\FlagClassifiers\\Netherlands Luxembourg Flag\\Flag_of_Luxembourg.svg.webp"))