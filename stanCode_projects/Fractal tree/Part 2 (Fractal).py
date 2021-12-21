import tkinter as tk
import math
point = []

top = tk.Tk()
top.title('Fractal')
top.resizable(False, False)
canvas = tk.Canvas(width=1300, height=700)
canvas.pack(side=tk.BOTTOM)
scale = tk.Scale(top)


def main():
    # 滑桿
    scale.config(orient="horizontal", length=300, from_=0, to=10, tickinterval=1, label="Level", command=draw)
    scale.pack()
    tk.mainloop()


def draw(val):
    level = int(val)
    canvas.delete("line")
    canvas.delete("flower")
    if 0 < level < 7:
        # h1 長度
        h = 600 / (1 + 3 * (1 - (3/4)**(level-1)))
    else:
        h = 600 / (1 + 3 * (1 - (3/4)**6))
    line(level, 0, canvas.winfo_width() / 2, canvas.winfo_height(), h, 15, math.pi / 2)


def line(level, count, x, y, length, width, theta):
    if level == count:
        pass
    elif level > 7 and count >= 7:
        # draw flower
        circle(x, y, 15, 4, count, level)
    else:
        # draw branch
        x2 = x - length * math.cos(theta)
        y2 = y - length * math.sin(theta)
        if count < 4:
            color = 'burlywood4'
        else:
            color = 'PaleGreen3'
        canvas.create_line(x, y, x2, y2, width=width, fill=color, tags="line")

        if count % 2 == 0:  # 偶數
            # right branch
            line(level, count+1, x2, y2, length * (3 / 4) * (2/(3**0.5)), width - 2, theta + (math.pi / 6))
            # left branch
            line(level, count+1, x2, y2, length * (3 / 4) * (2/(3**0.5)), width - 2, theta - (math.pi / 6))
        else: # 基數
            # right
            line(level, count + 1, x2, y2, length * 2 / (3 ** 0.5) * 9 / 16, width - 2, theta + (math.pi / 6))
            # left
            line(level, count + 1, x2, y2, length * 2 / (3 ** 0.5) * 9 / 16, width - 2, theta - (math.pi / 6))


def circle(x, y, r, w, count, level):
    if level == count:
        pass
    else:
        draw_circle(x, y, r, w)
        # left flower
        circle(x - r, y, r * 1/2, w - 1, count + 1, level)
        # left up flower
        circle(x - r/2, y - r * (3**0.5) / 2, r * 1 / 2, w - 1, count + 1, level)
        # right up flower
        circle(x + r/2, y - r * (3**0.5) / 2, r * 1 / 2, w - 1, count + 1, level)
        # right flower
        circle(x + r, y, r * 1 / 2, w - 1, count + 1, level)
        # right bottom flower
        circle(x + r/2, y + r*(3**0.5) / 2, r * 1 / 2, w - 1, count + 1, level)
        # left bottom flower
        circle(x - r / 2, y + r*(3**0.5) / 2, r * 1 / 2, w - 1, count + 1, level)


def draw_circle(x, y, r, w):
    canvas.create_oval(x-r, y-r, x+r, y+r, outline='PaleVioletRed1', tags='flower', width=w)


if __name__ == '__main__':
    main()
