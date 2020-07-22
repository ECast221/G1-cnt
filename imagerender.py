from PIL import Image


class ImageDisplayer(object):
    def __init__(self):
        pass

    def invert(self, img):
        return img.transpose(Image.FLIP_LEFT_RIGHT)
