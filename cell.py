from graphics import Window, Line, Point

class Cell:
    def __init__(self, win:Window) -> None:
        self.has_left_wall:bool = True
        self.has_right_wall:bool = True
        self.has_top_wall:bool = True
        self.has_bottom_wall:bool = True
        self.__x1:float = -1.0
        self.__x2:float = -1.0
        self.__y1:float = -1.0
        self.__y2:float = -1.0
        self.__win = win

    def draw(self, new_x1:float, new_y1:float, new_x2:float, new_y2:float) -> None:
        self.__x1 = new_x1
        self.__y1 = new_y1
        self.__x2 = new_x2
        self.__y2 = new_y2
        
        left = min(self.__x1, self.__x2)
        right = max(self.__x1, self.__x2)
        top = min(self.__y1, self.__y2)
        bottom = max(self.__y1, self.__y2)

        top_left = Point(left, top)
        top_right = Point(right, top)
        bottom_left = Point(left, bottom)
        bottom_right = Point(right, bottom)

        top_line = Line(top_left, top_right)
        bottom_line = Line(bottom_left, bottom_right)
        left_line = Line(top_left, bottom_left)
        right_line = Line(top_right, bottom_right)

        if self.has_top_wall:
            self.__win.draw_line(top_line)
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_line)
        if self.has_left_wall:
            self.__win.draw_line(left_line)
        if self.has_right_wall:
            self.__win.draw_line(right_line)
    
    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        fill_color:str = "red"
        if undo:
            fill_color = "gray"
        
        center_start = Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2)
        center_dest = Point((to_cell.__x1 + to_cell.__x2)/2, (to_cell.__y1 + to_cell.__y2)/2)

        move = Line(center_start, center_dest)
        self.__win.draw_line(move, fill_color)
