class Game:

    def __init__(self,board, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
        self.mov_ctr = 0

    def step(self):
        if self.board.turn == 1:
            self.board.makeMove(self.player_1.getMove())
            self.board.turn = 2
        else:
            self.board.makeMove(self.player_2.getMove())
            self.board.turn = 1

        self.mov_ctr += 1
