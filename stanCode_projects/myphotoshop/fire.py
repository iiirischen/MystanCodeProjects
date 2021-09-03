"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:str, the file path of the original colored image
    :return img_fire :Gray scaled image which marked the fire area in red
    """
    img_fire = SimpleImage(filename)
    for pixel in img_fire:
        avg = (pixel.red + pixel.green + pixel.blue)//3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel. blue = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return img_fire


def main():
    """
    This function can detect whether there is a forest fire and mark it out in red.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
