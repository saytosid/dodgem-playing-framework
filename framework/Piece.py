class Piece:
    def __init__(self,color='black',position=(-1,-1)):
        '''(-1,-1) means that piece is not on board, initial position of piece
        will be on row 1 or column 1 depending on color'''
        self.color = color
        self.pos = position
