"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return new_img :  SimpleImage, the blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_p = new_img.get_pixel(x, y)
            total_red = img.get_pixel(x, y).red
            total_green = img.get_pixel(x, y).green
            total_blue = img.get_pixel(x, y).blue
            if x == 0:
                if y == 0:
                    # ( 0,0 )
                    total_red = (total_red + img.get_pixel(1, 0).red + img.get_pixel(0, 1).red + img.get_pixel(1, 1).red) // 4
                    total_blue = (total_blue + img.get_pixel(1, 0).blue + img.get_pixel(0, 1).blue + img.get_pixel(1, 1).blue)//4
                    total_green = (total_green + img.get_pixel(1, 0).green + img.get_pixel(0, 1).green + img.get_pixel(1, 1).green)//4
                elif y == img.height-1:
                    # ( 0, height-1)
                    total_red = (total_red + img.get_pixel(0, img.height-2).red + img.get_pixel(1, img.height-1).red + img.get_pixel(1, img.height-2).red) // 4
                    total_blue = (total_blue + img.get_pixel(0, img.height-2).blue + img.get_pixel(1, img.height-1).blue+ img.get_pixel(1, img.height-2).blue) // 4
                    total_green = (total_green + img.get_pixel(0, img.height-2).green + img.get_pixel(1, img.height-1).green + img.get_pixel(1, img.height-2).green) // 4
                else:
                    # x = 0
                    total_red = (total_red + img.get_pixel(x, y-1).red + img.get_pixel(x+1, y-1).red + img.get_pixel(x+1, y).red + img.get_pixel(x, y+1).red + img.get_pixel(x+1,y+1).red)//6
                    total_blue = (total_blue + img.get_pixel(x, y-1).blue + img.get_pixel(x+1, y-1).blue + img.get_pixel(x+1, y).blue + img.get_pixel(x, y+1).blue + img.get_pixel(x+1,y+1).blue)//6
                    total_green = (total_green + img.get_pixel(x, y-1).green + img.get_pixel(x+1, y-1).green + img.get_pixel(x+1, y).green + img.get_pixel(x, y+1).green + img.get_pixel(x+1,y+1).green)//6
            elif y == 0:
                if x == 0:
                    # (0,0)
                    pass
                elif x == img.width-1:
                    # ( width-1, 0)
                    total_red = (total_red + img.get_pixel(x-1, 0).red + img.get_pixel(x-1, 1).red + img.get_pixel(x, 1).red) // 4
                    total_blue = (total_blue + img.get_pixel(x-1, 0).blue + img.get_pixel(x-1, 1).blue + img.get_pixel(x, 1).blue) // 4
                    total_green = (total_green + img.get_pixel(x-1, 0).green + img.get_pixel(x-1, 1).green + img.get_pixel(x, 1).green) // 4
                else:
                    # y = 0
                    total_red = (total_red + img.get_pixel(x-1,0).red + img.get_pixel(x+1,0).red + img.get_pixel(x-1,y+1).red + img.get_pixel(x,y+1).red + img.get_pixel(x+1,y+1).red) // 6
                    total_blue = (total_blue + img.get_pixel(x-1,0).blue + img.get_pixel(x+1,0).blue + img.get_pixel(x-1,y+1).blue + img.get_pixel(x,y+1).blue + img.get_pixel(x+1,y+1).blue) // 6
                    total_green = (total_green + img.get_pixel(x-1,0).green + img.get_pixel(x+1,0).green + img.get_pixel(x-1,y+1).green + img.get_pixel(x,y+1).green + img.get_pixel(x+1,y+1).green) // 6
            elif x == img.width-1:
                if y == 0:
                    # (width-1, 0)
                    pass
                elif y == img.height-1:
                    # (width-1, height-1)
                    total_red = (total_red + img.get_pixel(x-1,y-1).red + img.get_pixel(x,y-1).red + img.get_pixel(x-1,y).red) // 4
                    total_blue = (total_blue + img.get_pixel(x-1,y-1).blue + img.get_pixel(x,y-1).blue + img.get_pixel(x-1,y).blue) // 4
                    total_green = (total_green + img.get_pixel(x-1,y-1).green + img.get_pixel(x,y-1).green + img.get_pixel(x-1,y).green) // 4
                else:
                    # x = width-1
                    total_red = (total_red + img.get_pixel(x-1,y-1).red + img.get_pixel(x,y-1).red + img.get_pixel(x-1,y+1).red + img.get_pixel(x,y+1).red + img.get_pixel(x-1,y).red) // 6
                    total_blue = (total_blue + img.get_pixel(x-1,y-1).blue + img.get_pixel(x,y-1).blue + img.get_pixel(x-1,y+1).blue + img.get_pixel(x,y+1).blue + img.get_pixel(x-1,y).blue) // 6
                    total_green = (total_green + img.get_pixel(x-1,y-1).green + img.get_pixel(x,y-1).green + img.get_pixel(x-1,y+1).green + img.get_pixel(x,y+1).green + img.get_pixel(x-1,y).green)//6
            elif y == img.height-1:
                if x == 0:
                    # (0,height-1)
                    pass
                elif x == img.width-1:
                    # (width-1, height-1)
                    pass
                else:
                    # y = height-1
                    total_red = (total_red + img.get_pixel(x-1,y-1).red + img.get_pixel(x,y-1).red + img.get_pixel(x-1,y).red + img.get_pixel(x+1,y-1).red + img.get_pixel(x+1,y).red) // 6
                    total_blue = (total_blue + img.get_pixel(x-1, y-1).blue + img.get_pixel(x,y-1).blue + img.get_pixel(x-1,y).blue + img.get_pixel(x+1,y-1).blue + img.get_pixel(x+1,y).blue) // 6
                    total_green = (total_green + img.get_pixel(x-1,y-1).green + img.get_pixel(x,y-1).green + img.get_pixel(x-1,y).green + img.get_pixel(x+1,y-1).green + img.get_pixel(x+1,y).green)//6
            else:
                # the blanks in the middle
                total_red = (total_red + img.get_pixel(x-1,y).red + img.get_pixel(x+1,y).red + img.get_pixel(x-1,y-1).red + img.get_pixel(x,y-1).red + img.get_pixel(x+1,y-1).red+img.get_pixel(x-1,y+1).red+img.get_pixel(x,y+1).red++img.get_pixel(x+1,y+1).red)//9
                total_blue = (total_blue + img.get_pixel(x - 1, y).blue + img.get_pixel(x + 1, y).blue + img.get_pixel(x - 1, y - 1).blue + img.get_pixel(x, y - 1).blue + img.get_pixel(x + 1, y - 1).blue + img.get_pixel(x - 1, y + 1).blue + img.get_pixel(x, y + 1).blue + +img.get_pixel(x + 1, y + 1).blue) // 9
                total_green = (total_green + img.get_pixel(x - 1, y).green + img.get_pixel(x + 1, y).green + img.get_pixel(
                    x - 1, y - 1).green + img.get_pixel(x, y - 1).green + img.get_pixel(x + 1, y - 1).green + img.get_pixel(
                    x - 1, y + 1).green + img.get_pixel(x, y + 1).green + +img.get_pixel(x + 1, y + 1).green) // 9

            new_p.red = total_red
            new_p.blue =total_blue
            new_p.green = total_green
    return new_img


def main():
    """
    This function can output a blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
