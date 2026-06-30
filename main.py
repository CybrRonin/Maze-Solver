from graphics import Window, Point, Line
from cell import Cell

def main() -> None:
    win = Window(800, 600)

    pt1 = Point(55, 80)
    pt2 = Point(455, 536)
    pt3 = Point(58, 483)
    pt4 = Point(485, 230)

    line1 = Line(pt1, pt2)
    line2 = Line(pt3, pt4)

    win.draw_line(line1, "red")
    win.draw_line(line2, "black")

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(win)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)

    win.wait_for_close()

main()