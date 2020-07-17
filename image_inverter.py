from PIL import Image


class ImageInverter(object):
    def __init__(self):
        pass

    def invert(self, img):
        return img.transpose(Image.FLIP_LEFT_RIGHT)
