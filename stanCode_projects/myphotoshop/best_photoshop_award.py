"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.1

# Controls the upper bound for black pixel
BLACK_PIXEL = 240


def main():
    """
    Inspired by the  funny image of Buddhist monk , so I put myself in front of a light, means hoping.
    """
    fg = SimpleImage('image_contest/figure.JPG')
    bg = SimpleImage('image_contest/back.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(bg, fg):
    """
    : param1 bg: SimpleImage, the background image
    : param2 fg: SimpleImage, green screen figure image
    : return fg: SimpleImage, the image combine green screen and background image
    """
    for y in range(bg.height):
        for x in range(bg.width):
            fg_p = fg.get_pixel(x, y)
            total = fg_p.red + fg_p.blue + fg_p.green
            avg = total // 3
            if fg_p.green > avg * THRESHOLD and total > BLACK_PIXEL:
                bg_p = bg.get_pixel(x, y)
                fg_p.red = bg_p.red
                fg_p.blue = bg_p.blue
                fg_p.green = bg_p.green
    return fg

if __name__ == '__main__':
    main()
