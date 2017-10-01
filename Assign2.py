from framework import Board,Game,Player
import numpy as np
np.set_printoptions(suppress=True)

class MyPlayer(Player):

    def __init__(self):
        pass

    def get_move(self,board):
        '''
        :param board: Board object
        :return: (piece,new_position,BoardLeavingMove)
        '''
        moves = board.get_valid_moves()
        return moves[0]

if __name__=='__main__':
    board = Board(size=5)
    player_1 = Player() # Random player
    player_2 = MyPlayer() # MyPlayer

    game = Game(board,player_1,player_2)

    while (game.step()==0):
        board_matrix,turn = board.get_board_config()
        print(board_matrix)
        print(" ")

