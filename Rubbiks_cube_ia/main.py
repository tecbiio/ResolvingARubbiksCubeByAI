from movement import movement
from cube import cube
from resolve_ia import neural_network

cube = cube()
move = movement()
neural_network = neural_network()

cube.show_main_side()
move.right(cube)
cube.show_main_side()
move.right(cube)
cube.show_main_side()
move.right(cube)
cube.show_main_side()
move.right(cube)
cube.show_main_side()
move.left(cube)
cube.show_main_side()
move.left(cube)
cube.show_main_side()

print("Neural network: ")
print(neural_network.w1)
print(neural_network.w2)

o = neural_network.forward(cube)