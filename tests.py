import unittest
from maze import Maze
import random

class WindowMock:
    def __init__(self, width, height):
        pass

    def redraw(self):
        pass

    def wait_for_close(self):
        pass

    def close(self):
        pass

    def draw_line(self, line, fill_color):
        pass

class Tests(unittest.TestCase):
    # def test_maze_create_cells(self):
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(len(m1.cells), num_rows)
    #     self.assertEqual(len(m1.cells[0]), num_cols)

    # def test_maze_cells_equal_dimensions(self):
    #     num_cols = 12
    #     num_rows = 31
    #     cell_x = 31
    #     cell_y = 1
    #     m = Maze(320, 211, num_rows, num_cols, cell_x, cell_y)

    #     for i, row in enumerate(m.cells):
    #         for j, cell in enumerate(row):
    #             self.assertEqual(cell.x1, m.x1 + j * cell_x)
    #             self.assertEqual(cell.x2, m.x1 + (j + 1) * cell_x)
    #             self.assertEqual(cell.y1, m.y1 + i * cell_y)
    #             self.assertEqual(cell.y2, m.y1 + (i + 1) * cell_y)
    
    # def test_break_entrance_and_exit(self):
    #     m = Maze(31, 22, 34, 71, 132, 61)
    #     self.assertEqual(m.cells[0][0].has_top_wall, False)
    #     self.assertEqual(m.cells[-1][-1].has_bottom_wall, False)

    # def test_maze_reset_cells_visited(self):
    #     m = Maze(30, 21, 10, 10, 32, 32)
    #     for row in m.cells:
    #         for cell in row:
    #             self.assertFalse(cell.visited)

    def test_maze_solve(self):
        fails = 0
        for i in range(1000):
            m = Maze(0, 0, random.randint(10, 40), random.randint(10, 40), 10, 10, WindowMock(0, 0))
            if not m.solve():
                fails += 1

        self.assertEqual(fails, 0)



if __name__ == "__main__":
    unittest.main()