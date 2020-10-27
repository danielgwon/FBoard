# Author: Daniel Gwon
# Date: 11/28/2019
# Description:


class FBoard:

    """"""

    def __init__(self):
        """"""
        self._board = [['','','','x','','','',''],['','','','','','','',''],
                       ['','','','','','','',''],['','','','','','','',''],
                       ['','','','','','','',''],['','','','','','','',''],
                       ['','','','','','','',''],['o','','o','','o','','o','']]
        self._game_state = "UNFINISHED"
        self._x_row = 0
        self._x_column = 3

    def get_game_state(self):
        """returns the current value of game_state"""
        return self._game_state

    def print_board(self):                  # DELETE
        """prints board for debugging purposes"""
        for i in range(8):
            print(self._board[i])

    def move_x(self, row, column):
        """moves x to a new position and updates state if necessary"""

        # if game_state is X_WON or O_WON, the game is over
        if self.get_game_state() != "UNFINISHED":
            return False

        # check if row or column are out of bounds
        if (row < 0 or row > 7) or (column < 0 or column > 7):
            return False

        # check if position is occupied
        if self._board[row][column] != '':
            return False

        # if the move is diagonal, move x
        if row > (self._x_row+1) or row < (self._x_row-1):
            return False
        elif column > (self._x_column+1) or column < (self._x_column-1):
            return False
        else:                                      # move x to desired position
            self._board[self._x_row][self._x_column] = ''  # clear old position
            self._x_row = row
            self._x_column = column
            self._board[self._x_row][self._x_column] = 'x'  # move x
            if self._x_row == 7:
                self._game_state = "X_WON"
                return True

    def move_o(self, row_from, column_from, row_to, column_to):
        """"""

        # if game_state is X_WON or O_WON, the game is over
        if self.get_game_state() != "UNFINISHED":
            return False

        # check if row or column are out of bounds
        if (row_to < 0 or row_to > 7) or (column_to < 0 or column_to > 7):
            return False

        # check if position is occupied
        if self._board[row_to][column_to] != '':
            return False

        # check if o is in the starting position
        if self._board[row_from][column_from] != 'o':
            return False

        # if row doesn't increase and move is diagonal, move o
        if row_to > row_from:
            return False
        elif column_to != (column_from+1) and column_to != (column_from-1):
            return False
        else:
            self._board[row_from][column_from] = ''
            self._board[row_to][column_to] = 'o'

        # x position tuples
        x_positions = []

        = (self._x_row-1, self._x_column-1)
        x_position_2 = (self._x_row-1, self._x_column+1)
        x_position_3 = (self._x_row+1, self._x_column-1)
        x_position_4 = (self._x_row+1, self._x_column+1)

        # check position one
        if x_row-1 >= 0 and x_col-1 >= 0:
            if self._board[x_row-1][x_col-1] != '':
                x_positions[0] = False
        # check position two
        if x_row-1 >= 0 and x_col+1 <= 7:
            if self._board[x_row-1][x_col+1] = '':
                self._game_state = "UNFINISHED"
        elif x_row+1 <= 7:
            if x_col-1 >= 0:
                if self._board[x_row+1][x_col-1] = '':
                    self._game_state = "UNFINISHED"
            elif x_col+1 <= 7:
                if self._board[x_row+1][x_col+1] = '':
                    self._game_state = "UNFINISHED"
        else:
            self._game_state = "O_WON"

        return True


fb = FBoard()
fb.print_board()
print(fb.move_o(7, 1))