from cell import Cell
import time
import random
class Maze:

    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols,
            cell_size_x,
            cell_size_y,
            window = None,
            solve_color="red",
            undo_color="gray",
            seed = None
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.solve_color = solve_color
        self.undo_color = undo_color
        self.window = window
        if seed is not None:
            random.seed(seed)
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_wall_r(0, 0)
        self.reset_cells_visited()

    def create_cells(self):
        self.cells = [[Cell(self.x1 + i*self.cell_size_x, self.y1 + j*self.cell_size_y, self.x1 + (i + 1) * self.cell_size_x, self.y1 + (j + 1) * self.cell_size_y, self.window) for i in range(self.num_cols)] for j in range(self.num_rows)]

    def reset_cells_visited(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False

    def draw_cell(self, i, j):
        if self.window is None:
            return
        self.cells[i][j].draw("black")
        self.animate()

    def animate(self):
        self.window.redraw()
        # time.sleep(0.01)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[-1][-1].has_bottom_wall = False
        self.draw_cell(self.num_rows-1, self.num_cols-1)

    def break_wall_r(self, i, j):
        current_cell = self.cells[i][j]
        current_cell.visited = True
        while True:
            possible_directions = []
            for x in [-1, 1]:
                if j + x < 0 or j + x >= self.num_cols:
                    continue
                if not self.cells[i][j + x].visited:
                    possible_directions.append((i, j + x))
            for y in [-1, 1]:
                if i + y < 0 or i + y >= self.num_rows:
                    continue
                if not self.cells[i + y][j].visited:
                    possible_directions.append((i + y, j))

            if len(possible_directions) == 0:
                self.draw_cell(i, j)
                return
            
            direction = random.choice(possible_directions)
            next_cell = self.cells[direction[0]][direction[1]]
            if direction[1] == j - 1:
                next_cell.has_right_wall = False
                current_cell.has_left_wall = False
            if direction[1] == j + 1:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            
            if direction[0] == i - 1:
                next_cell.has_bottom_wall = False
                current_cell.has_top_wall = False
            if direction[0] == i + 1:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            
            self.break_wall_r(direction[0], direction[1])


    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self.animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        
        if j - 1 >= 0 and not current_cell.has_left_wall and not self.cells[i][j-1].has_right_wall and not self.cells[i][j-1].visited:
            current_cell.draw_move(self.cells[i][j-1], self.solve_color)
            if self.solve_r(i, j-1):
                return True
            current_cell.draw_move(self.cells[i][j-1], self.undo_color, True)

        if j + 1 < self.num_cols and not current_cell.has_right_wall and not self.cells[i][j+1].has_left_wall and not self.cells[i][j+1].visited:
            current_cell.draw_move(self.cells[i][j+1], self.solve_color)
            if self.solve_r(i, j+1):
                return True
            current_cell.draw_move(self.cells[i][j+1], self.undo_color, True)

        if i - 1 >= 0 and not current_cell.has_top_wall and not self.cells[i-1][j].has_bottom_wall and not self.cells[i-1][j].visited:
            current_cell.draw_move(self.cells[i-1][j], self.solve_color)
            if self.solve_r(i-1, j):
                return True
            current_cell.draw_move(self.cells[i-1][j], self.undo_color, True)

        if i + 1 < self.num_rows and not current_cell.has_bottom_wall and not self.cells[i+1][j].has_top_wall and not self.cells[i+1][j].visited:
            current_cell.draw_move(self.cells[i+1][j], self.solve_color)
            if self.solve_r(i+1, j):
                return True
            current_cell.draw_move(self.cells[i+1][j], self.undo_color, True)
        
        return False
