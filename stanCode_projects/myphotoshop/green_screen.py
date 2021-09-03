"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: MillenniumFalcon.png, the background image
    :param figure_img: the green screen image
    :return: the image that uses background_img to replace the green pixel in figure_img
    """
    background_img.make_as_big_as(figure_img)
    for x in range(background_img.width):
        for y in range(background_img.height):
            bg_p = background_img.get_pixel(x, y)
            fig_p = figure_img.get_pixel(x, y)
            bigger = max(fig_p.red, fig_p.blue)
            if fig_p.green > bigger*2:
                fig_p.green = bg_p.green
                fig_p.blue = bg_p.blue
                fig_p.red = bg_p.red
    return figure_img


def main():
    """
    This function combines two image into one.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
