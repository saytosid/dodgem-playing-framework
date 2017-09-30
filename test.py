from framework import Board
import numpy as np

board = Board(size=3)

board_matrix,turn = board.get_board_config()
np.set_printoptions(suppress=True)
print(board_matrix)
print('Turn: Player_'+str(turn))

for item in board.get_valid_moves():
    print [item[0].pos,item[1]]

