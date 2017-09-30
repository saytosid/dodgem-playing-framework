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

    def get_board_config(self):
        '''Returns tupple (board_configuration,turn)'''
        import numpy as np
        board_matrix = np.zeros((self.size,self.size))
        for piece in self.player_1_pieces:
            board_matrix[piece.pos[0],piece.pos[1]] = 1
        for piece in self.player_2_pieces:
            board_matrix[piece.pos[0],piece.pos[1]] = 2

        return (board_matrix, self.turn)

    def get_valid_moves(self):
        board_matrix,turn = self.get_board_config()
        valid_moves = [] # A move is a tupple of the form (Piece,(new_position_tuple))
        if self.turn == 1:
            for piece in self.player_1_pieces:
                pos = piece.pos
                forward_move = (pos[0],pos[1]+1) # towards right for player_1
                if forward_move[1] < self.size and board_matrix[forward_move] == 0:
                    # if new position is unoccupied and piece doesnt jump off the board
                    valid_moves.append((piece,forward_move))
                elif forward_move[1] == self.size:
                    # Piece can leave the board
                    valid_moves.append((piece,forward_move))

                sideways_left = (pos[0]-1,pos[1])
                if board_matrix[sideways_left] == 0 and sideways_left != (self.size-1,0) and sideways_left[0] != -1:
                    # Piece doesnt go to bottom left corner, doesnt leave board and moves on empty block
                    valid_moves.append((piece,sideways_left))

                sideways_right = (pos[0]+1,pos[1])
                if sideways_right != (self.size-1,0) and sideways_left[0] != -1 and board_matrix[sideways_right] == 0:
                    # Piece doesnt go to bottom, doesnt leave board left corner and moves on empty block
                    valid_moves.append((piece,sideways_right))


        return valid_moves
