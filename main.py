from tkinter import Tk, BOTH, Canvas
from maze import Maze
class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Window")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False


    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


def main():
    window = Window(1200, 900)

    maze = Maze(200, 50, 40, 40, 20, 20, window)
    print("Solving...")
    solved = maze.solve()
    print("Solved!" if solved else "Failed!")
    
    window.wait_for_close()


if __name__ == "__main__":
    main()
