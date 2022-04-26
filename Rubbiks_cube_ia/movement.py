class movement:
    def right(self, cube):
        tmp1 = cube.grid[0, 0, 2]
        tmp2 = cube.grid[0, 1, 2]
        tmp3 = cube.grid[0, 2, 2]

        cube.grid[0, 0, 2] = cube.grid[5, 0, 2]
        cube.grid[0, 1, 2] = cube.grid[5, 1, 2]
        cube.grid[0, 2, 2] = cube.grid[5, 2, 2]

        cube.grid[5, 0, 2] = cube.grid[2, 0, 0]
        cube.grid[5, 1, 2] = cube.grid[2, 1, 0]
        cube.grid[5, 2, 2] = cube.grid[2, 2, 0]

        cube.grid[2, 0, 0] = cube.grid[4, 0, 0]
        cube.grid[2, 1, 0] = cube.grid[4, 1, 0]
        cube.grid[2, 2, 0] = cube.grid[4, 2, 0]

        cube.grid[4, 0, 0] = tmp3
        cube.grid[4, 1, 0] = tmp2
        cube.grid[4, 2, 0] = tmp1

    def left(self, cube):
        tmp1 = cube.grid[0, 0, 0]
        tmp2 = cube.grid[0, 1, 0]
        tmp3 = cube.grid[0, 2, 0]

        cube.grid[0, 0, 0] = cube.grid[5, 0, 0]
        cube.grid[0, 1, 0] = cube.grid[5, 1, 0]
        cube.grid[0, 2, 0] = cube.grid[5, 2, 0]

        cube.grid[5, 0, 0] = cube.grid[2, 0, 2]
        cube.grid[5, 1, 0] = cube.grid[2, 1, 2]
        cube.grid[5, 2, 0] = cube.grid[2, 2, 2]

        cube.grid[2, 0, 2] = cube.grid[4, 0, 2]
        cube.grid[2, 1, 2] = cube.grid[4, 1, 2]
        cube.grid[2, 2, 2] = cube.grid[4, 2, 2]

        cube.grid[4, 0, 2] = tmp3
        cube.grid[4, 1, 2] = tmp2
        cube.grid[4, 2, 2] = tmp1