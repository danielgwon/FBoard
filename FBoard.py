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

        # check if the move is diagonal
        if row > (self._x_row+1) or row < (self._x_row-1):
            return False
        elif column > (self._x_column+1) or column < (self._x_column-1):
            return False
        else:                               # move x to desired position
            self._board[self._x_row][self._x_column] = ''       # clear old position
            self._x_row = row
            self._x_column = column
            self._board[self._x_row][self._x_column] = 'x'      # move x to new position
            if self._x_row == 7:
                self._game_state = "X_WON"
                return True

    def move_o(self, row_from, column_from, row_to, column_to):
        """"""

        # check if row or column are out of bounds
        if (row < 0 or row > 7) or (column < 0 or column > 7):
            return False

        # if state is X_WON or O_WON, the game is over
        if state != "UNFINISHED":
            return False


fb = FBoard()
fb.print_board()
print(fb.move_x(7, 1))