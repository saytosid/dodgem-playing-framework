from Piece import Piece


class Board:
    def __init__(self,size = 3):
        self.size = size
        self.turn = 1 # Player 1 goes first
        self.player_1_pieces = []
        for i in xrange(size):
            if i != size-1:
                self.player_1_pieces.append(Piece(color='black',position=(i,0)))

        self.player_2_pieces = []
        for i in xrange(size):
            if i != 0:
                self.player_2_pieces.append(Piece(color='white',position=(size-1,i)))

    def draw_board(self):
        '''Prints current board configuration'''
        import numpy as np
        board_matrix = np.zeros((self.size,self.size))
        for piece in self.player_1_pieces:
            board_matrix[piece.pos[0],piece.pos[1]] = 1
        for piece in self.player_2_pieces:
            board_matrix[piece.pos[0],piece.pos[1]] = 2
        np.set_printoptions(suppress=True)
        print(board_matrix)
        print('Turn: Player_'+str(self.turn))
