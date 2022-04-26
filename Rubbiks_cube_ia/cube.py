from xmlrpc.client import Boolean
import numpy as np

class cube:
    def __init__(self) -> None:
        grid = np.zeros((6, 3, 3))
        for i in range(0, 6):
            grid[i, :, :] = i
        self.grid = grid

    def show_main_side(self) -> None:
        print(self.grid[0])
        print(self.is_sort())
        print("")

    def is_sort(self) -> Boolean:
        for i in range(0, 6):
            tmp = self.grid[i, 1, 1]
            for j in range(0, 3):
                for k in range(0, 3):
                    if not (self.grid[i, j, k] == tmp):
                        return False
        return True

