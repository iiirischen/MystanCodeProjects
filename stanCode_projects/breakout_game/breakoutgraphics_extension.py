"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.__paddle = GRect(paddle_width, paddle_height)
        self.__paddle.filled = True
        self.window.add(self.__paddle, (window_width-paddle_width)/2, window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2, (self.window.height - self.ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start)
        onmousemoved(self.move_paddle)

        # Draw scoreboard
        self.score = 0
        self._score_label = GLabel('Score: '+str(self.score))
        self._score_label.font = '-30'
        self.window.add(self._score_label, 0, self._score_label.height)

        # Draw bricks
        self._brick_nums = brick_cols*brick_rows
        for x in range(brick_cols):
            for y in range(brick_rows):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if (y % 2 == 0 and (y / 2) % 6 == 0) or (y % 2 == 1 and y % 12 == 1):       # create red bricks at first and second columns
                    brick.fill_color = 'red'
                    brick.color = 'red'
                elif (y % 2 == 0 and (y / 2) % 6 == 1) or (y % 2 == 1 and y % 12 == 3):     # create orange bricks at third and forth columns
                    brick.fill_color = 'orange'
                    brick.color = 'orange'
                elif (y % 2 == 0 and (y / 2) % 6 == 2) or (y % 2 == 1 and y % 12 == 5):     # create yellow bricks at fifth and sixth columns
                    brick.fill_color = 'yellow'
                    brick.color = 'yellow'
                elif (y % 2 == 0 and (y / 2) % 6 == 3) or (y % 2 == 1 and y % 12 == 7):     # create green bricks at seventh and eighth columns
                    brick.fill_color = 'green'
                    brick.color = 'green'
                elif (y % 2 == 0 and (y / 2) % 6 == 4) or (y % 2 == 1 and y % 12 == 9):     # create blue bricks at ninth and tenth columns
                    brick.fill_color = 'blue'
                    brick.color = 'blue'
                elif (y % 2 == 0 and (y / 2) % 6 == 5) or (y % 2 == 1 and y % 12 == 11):    # create purple bricks at eleventh and twelfth columns
                    brick.fill_color = 'purple'
                    brick.color = 'purple'
                self.window.add(brick, (brick_width + brick_spacing)*x, brick_offset+(brick_height+brick_spacing)*y)

    def reset_ball(self):
        """
        reset the ball's position and velocity
        """
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2, (self.window.height - self.ball.height) / 2)
        self.__dx = 0
        self.__dy = 0

    def move_paddle(self, mouse):
        """
        This function uses to connect the mouse and the paddle,
        the mouse will control left and right move of the paddle
        """
        self.__paddle.x = mouse.x-self.__paddle.width/2
        if self.__paddle.x < 0:     # when the mouse goes beyond right window, paddle will stop at the rightmost
            self.__paddle.x = 0
        elif self.__paddle.x+self.__paddle.width > self.window.width:  # when the mouse goes beyond left window, paddle will stop at the rightmost
            self.__paddle.x = self.window.width-self.__paddle.width

    def set_ball_velocity(self):
        """
        This function randomly generated speed of x-axis
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx *= -1

    def get_dx(self):
        """
        :return: the x-axis speed
        """
        return self.__dx

    def get_dy(self):
        """
        :return: the y-axis speed
        """
        return self.__dy

    def get_brick_nums(self):
        """
        :return: the total numbers of bricks
        """
        return self._brick_nums

    def start(self, mouse):
        """
        This function controls whether the ball starts moving
        """
        if self.__dx == 0:
            self.set_ball_velocity()

    def hit_the_wall(self):
        """
        when the ball hits the left or right or top side of the window,
        the ball will rebound
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1
        if self.ball.y <= 0:
            self.__dy *= -1

    def hit_the_bottom(self):
        """
        when the ball hit the bottom of the window, the game will reset
        """
        if self.ball.y > self.window.height:
            self.reset_ball()
            return True

    def hit_sth(self):
        """
        if the ball hits paddle, the ball will rebound
        if the ball  hits bricks, the ball will rebound and also destroy the bricks
        """
        left_top = self.window.get_object_at(self.ball.x, self.ball.y)                                          # coordinate of upper left corner
        right_top = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)                         # coordinate of upper right corner
        left_bottom = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)                      # coordinate of the lower left corner
        right_bottom = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)     # coordinate of lower right corner

        if left_top or right_top or left_bottom or right_bottom is not None:
            if left_bottom is self.__paddle:
                self.__dy *= -1
                self.ball.y = self.__paddle.y - self.ball.height
            elif right_bottom is self.__paddle:
                self.__dy *= -1
                self.ball.y = self.__paddle.y - self.ball.height
            elif left_top is self.__paddle:
                self.__dy *= -1
                self.ball.y = self.__paddle.y + self.__paddle.height
            elif right_top is self.__paddle:
                self.__dy *= -1
                self.ball.y = self.__paddle.y + self.__paddle.height
            elif left_top is self._score_label:
                pass
            elif right_top is self._score_label:
                pass
            elif left_bottom is self._score_label:
                pass
            elif right_bottom is self._score_label:
                pass
            else:
                if left_top is not None:
                    self.__dy *= -1
                    self.window.remove(left_top)
                    self._brick_nums -= 1
                    self.score += 1
                    self._score_label.text = 'Score: '+str(self.score)
                elif right_top is not None:
                    self.__dy *= -1
                    self.window.remove(right_top)
                    self._brick_nums -= 1
                    self.score += 1
                    self._score_label.text = 'Score: '+str(self.score)
                elif left_bottom is not None:
                    self.__dy *= -1
                    self.window.remove(left_bottom)
                    self._brick_nums -= 1
                    self.score += 1
                    self._score_label.text = 'Score: '+str(self.score)
                elif right_bottom is not None:
                    self.__dy *= -1
                    self.window.remove(right_bottom)
                    self._brick_nums -= 1
                    self.score += 1
                    self._score_label.text = 'Score: '+str(self.score)



