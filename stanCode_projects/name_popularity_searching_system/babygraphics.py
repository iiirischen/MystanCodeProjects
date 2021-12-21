"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
This program will draw the searching result on window
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000

# global variable
x_spacing = (CANVAS_WIDTH-GRAPH_MARGIN_SIZE-GRAPH_MARGIN_SIZE)/len(YEARS)   # spacing between x coordinates
y_spacing = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE-GRAPH_MARGIN_SIZE)/1000        # spacing between y coordinates


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    global x_spacing
    x_coordinate = GRAPH_MARGIN_SIZE+x_spacing*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    global x_spacing, y_spacing
    y = [0, 0]  # y coordinate
    x = [0, 0]  # x coordinate
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        while i > len(COLORS)-1:    # let the color keep looping
            i -= len(COLORS)
        for j in range(len(YEARS)):
            year = str(YEARS[j])
            x[0] = GRAPH_MARGIN_SIZE+x_spacing*j
            if year not in name_data[name] or int(name_data[name][year]) >= 1000:
                """
                if the year is not in name_data or the rank of the year is more han 1000, the text will use * instead of 
                the year
                """
                y[0] = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(x[0] + TEXT_DX, y[0], text=name + "*", anchor=tkinter.SW, fill=COLORS[i])
            else:
                y[0] = GRAPH_MARGIN_SIZE + y_spacing * int(name_data[name][year])
                canvas.create_text(x[0] + TEXT_DX, y[0], text=name + str(name_data[name][year]), anchor=tkinter.SW,
                                   fill=COLORS[i])
            if j > 0:
                canvas.create_line(x[1], y[1], x[0], y[0], width=LINE_WIDTH, fill=COLORS[i])
            y[1] = y[0]
            x[1] = x[0]


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
