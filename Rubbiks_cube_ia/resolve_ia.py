import numpy as np
from movement import movement
from cube import cube

cube = cube()
move = movement()

move.left(cube)
move.left(cube)
move.right(cube)
move.right(cube)
move.right(cube)

# initial state of cube
# let ai sort it !

class neural_network(object):
    def __init__(self) -> None:
        self.input_size = 1
        self.output_size = 1
        self.hidden_size = 12

        self.w1 = np.random.randn(self.input_size, self.hidden_size) # Matrix 12*1 - entry
        self.w_intermediate = [] # np.random.randn(self.hidden_size, self.hidden_size) # Matrix 12*12 - intermediate
        self.w2 = np.random.randn(self.hidden_size, self.output_size) # Matrix 1*12 - exit

        self.z_intermediate = []

    def forward(self, cube):
        max = 0
        pos = 0

        for i in range(0, 11):
            if max < self.w1[i]:
                max = self.w1[i]
                pos = i

        if pos == 0:
            move.right(cube)
        elif pos == 1:
            move.left(cube)


        while not cube.is_sort():
            self.w_intermediate.append(np.random.randn(self.hidden_size, self.hidden_size)) # Adding a deep level

            # recursivity ?
            self.z = np.dot(x, self.w1)
            self.z2 = self.sigmoid(self.w2)

            if len(self.w_intermediate) == 1:
                self.z_intermediate.append(np.dot(self.z2, self.w_intermediate[0]))
            else:
                self.z_intermediate.append(np.dot(self.w_intermediate[len(self.w_intermediate)-2], self.w_intermediate[len(self.w_intermediate)-1]))


        self.z3 = np.dot(self.w_intermediate[len(self.w_intermediate)-1], self.w2)

        o = self.sigmoid(self.z3)

        # return o
            


        

    def sigmoid(self, s):
        return 1/(1+np.exp(-s))