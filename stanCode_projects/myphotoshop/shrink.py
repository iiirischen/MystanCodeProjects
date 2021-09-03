"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return new_img: SimpleImage, the image which has half the width and height of the original
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width*1//2, img.height*1//2)
    for x in range(new_img.width):
        for y in range(new_img.height):
            new_img.get_pixel(x, y).red = img.get_pixel(x*2, y*2).red
            new_img.get_pixel(x, y).blue = img.get_pixel(x*2, y*2).blue
            new_img.get_pixel(x, y).green = img.get_pixel(x*2, y*2).green
    return new_img


def main():
    """
    This function can make the width and the height of the image shrink twice
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
