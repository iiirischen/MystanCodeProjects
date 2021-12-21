"""
File: blur.py
Name:Iris chen
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:SimpleImage, the original image
    :return:SimpleImage, the blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            count = 0
            # count how many neighbors pixel has
            new_p = new_img.get_pixel(x, y)
            total_red = 0
            # add all the red pixels together
            total_green = 0
            # add all the green pixels together
            total_blue = 0
            # add all the blue pixels together
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    # find adjacent points
                    if i < 0 or j < 0 or i > img.width-1 or j > img.height-1:
                        # exclude points that are not in the range
                        pass
                    else:
                        total_red += img.get_pixel(i, j).red
                        total_blue += img.get_pixel(i, j).blue
                        total_green += img.get_pixel(i, j).green
                        count += 1
            new_p.red = total_red//count
            new_p.blue = total_blue//count
            new_p.green = total_green//count
    return new_img


def main():
    """
    TODO:This function can output a blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
