"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by  
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    THis is a breakout game, user has 3 chances.
    The user needs to try his best to destroy all the bricks.
    When the ball hit the wall or bricks or paddle, the ball will rebound.
    The extension file adds the function of scoreboard
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add animation loop here!
    while True:
        if lives <= 0:
            break
        if graphics.get_brick_nums() == 0:              # if destroy all the bricks, the game ended
            break
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.hit_the_wall()
        graphics.hit_sth()
        if graphics.hit_the_bottom():
            lives -= 1
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
