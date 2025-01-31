from graphics import Line, Point
class Cell:
    
    def __init__(self, x1, y1, x2, y2, window=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, color):
        if self.window is None:
            return
        x = min(self.x1, self.x2)
        line = Line(Point(x, self.y1), Point(x, self.y2))
        self.window.draw_line(line, "white")
        if self.has_left_wall:
            self.window.draw_line(line, color)

        x = max(self.x1, self.x2)
        line = Line(Point(x, self.y1), Point(x, self.y2))
        self.window.draw_line(line, "white")
        if self.has_right_wall:
            self.window.draw_line(line, color)

        y = min(self.y1, self.y2)
        line = Line(Point(self.x1, y), Point(self.x2, y))
        self.window.draw_line(line, "white")
        if self.has_top_wall:
            self.window.draw_line(line, color)

        y = max(self.y1, self.y2)
        line = Line(Point(self.x1, y), Point(self.x2, y))
        self.window.draw_line(line, "white")
        if self.has_bottom_wall:
            self.window.draw_line(line, color)

    def draw_move(self, to_cell, color, undo=False):
        x1 = (self.x1 + self.x2) / 2
        y1 = (self.y1 + self.y2) / 2
        
        x2 = (to_cell.x1 + to_cell.x2) / 2
        y2 = (to_cell.y1 + to_cell.y2) / 2

        line = Line(Point(x1, y1), Point(x2, y2))
        # self.window.draw_line(line, "gray" if undo else "red")
        self.window.draw_line(line, color)