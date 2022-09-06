import urllib.request
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import os

def image_from_url(url, color_conversion=None, resize=None):
    req = urllib.request.urlopen(url)
    img = Image.open(req)

    if (color_conversion != None):
        img = img.convert(color_conversion)
    if (resize != None):
        img = img.resize(resize)

    return img

def view_random_image(target_dir, target_class):
    target_folder = target_dir + "/" + target_class

    random_image = random.sample(os.listdir(target_folder), 1)

    img = mpimg.imread(target_folder + "/" + random_image[0])

    fig, ax = plt.subplots(figsize=(10,10))
    plt.title(target_class)
    ax.imshow(img)
    ax.axis("off");

    return img