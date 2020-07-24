"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Melina Ferner.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    # Store values for bottom rectangle:
    ulc_coordinates_bottom_rect = rectangle.get_upper_left_corner()
    ulc_x_bottom_rect = ulc_coordinates_bottom_rect.x
    ulc_y_bottom_rect = ulc_coordinates_bottom_rect.y
    lrc_coordinates_bottom_rect = rectangle.get_lower_right_corner()
    lrc_x_bottom_rect = lrc_coordinates_bottom_rect.x
    lrc_y_bottom_rect = lrc_coordinates_bottom_rect.y
    width = rectangle.get_width()
    height = rectangle.get_height()
    # print(ulc_x_bottom_rect, ulc_y_bottom_rect, lrc_x_bottom_rect, lrc_y_bottom_rect)

    # Find upper left corner and lower right corner for top/leftmost rectangle:
    ulc_x_ref = ulc_x_bottom_rect - (n-1)*0.5*width
    ulc_y_ref = ulc_y_bottom_rect - (n-1)*height
    lrc_x_ref = lrc_x_bottom_rect - (n-1)*0.5*width
    lrc_y_ref = lrc_y_bottom_rect - (n-1)*height

    # Loop to create wall:
    for k in range(n, 0, -1):
        for j in range(k):
            ulc_x = ulc_x_ref + j*width
            lrc_x = lrc_x_ref + j*width
            new_rectangle = rg.Rectangle(rg.Point(ulc_x, ulc_y_ref), rg.Point(lrc_x, lrc_y_ref))
            new_rectangle.attach_to(window)
        # if k == 1:
            # print(ulc_x_ref, ulc_y_ref, lrc_x_ref, lrc_y_ref)
        ulc_x_ref = ulc_x_ref + 0.5*width
        ulc_y_ref = ulc_y_ref + height
        lrc_x_ref = lrc_x_ref + 0.5*width
        lrc_y_ref = lrc_y_ref + height
    window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
