from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width:int, height:int) -> None:
        self.__root = Tk()
        self.__root.geometry(str(width)+'x'+str(height))
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self) -> None:
        self.__running = False
    
    def draw_line(self, new_line:"Line", fill_color:str = "black") -> None:
        new_line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, start:Point, end:Point) -> None:
        self.__start = start
        self.__end = end
    
    def draw(self, dest:Canvas, fill_color:str = "black") -> None:
        dest.create_line(self.__start.x, self.__start.y, self.__end.x, self.__end.y, fill=fill_color, width=2)
