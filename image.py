import urllib.request
from PIL import Image
def image_from_url(url, color_conversion=None, resize=None):
    req = urllib.request.urlopen(url)
    img = Image.open(req)

    if (color_conversion != None):
        img = img.convert(color_conversion)
    if (resize != None):
        img = img.resize(resize)

    return img
