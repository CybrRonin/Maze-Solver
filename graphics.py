from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width:int, height:int) -> None:
        self.__root = Tk()
        self.__root.geometry(str(width)+'x'+str(height))
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH)
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
