"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:str, the file path of the original image
    :return blank_img: a vertical mirror image
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            blank_p1 = blank_img.get_pixel(x, y)
            blank_p2 = blank_img.get_pixel(x, blank_img.height-y-1)

            blank_p1.red = img_p.red
            blank_p1.green = img_p.green
            blank_p1.blue = img_p.blue

            blank_p2.red = img_p.red
            blank_p2.green = img_p.green
            blank_p2.blue = img_p.blue
    return blank_img


def main():
    """
    This function can output a mirror image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
