# import pygame
from constants import *
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width           # should be 675 (roughly based on TTT.gui)
        self.height = height           # made 675 instead of 600 to be easily divisible by 9
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):     # a function to draw all the starting lines on the board
        for i in range(1, 4):           # make a for loop to make the necessary number of horizontal lines (8)
            pygame.draw.line(                   # designated function from pygame takes these parameters
                self.screen,                         # where it is being displayed
                line_color,                           # the color of the line (dark black)
                (0, i * box_dimension),             # the x/y coordinates of the startpoint of the line
                (675, i * box_dimension),           # the x/y coordinates of the endpoint of the line
                box_line_width                      # the width (thickness) of the line (taken from TTT.gui)
            )

        for j in range(1, 4):           # make a for loop to make the necessary number of horizontal lines (8)
            pygame.draw.line(                   # designated function from pygame takes these parameters
                self.screen,                         # where it is being displayed
                line_color,                           # the color of the line (dark black)
                (j * box_dimension, 0),               # the x/y coordinates of the startpoint of the line
                (j * box_dimension, board_dimension),           # the x/y coordinates of the endpoint of the line
                box_line_width                          # the width (thickness) of the line (taken from TTT.gui)
            )

        for k in range(1, 9):           # make a for loop to draw horizontal cell lines (9 total)
            pygame.draw.line(                   # designated function from pygame takes these parameters
                self.screen,                         # where it is being displayed
                line_color,                           # the color of the line (dark black)
                (0, k * cell_dimension),               # the x/y coordinates of the startpoint of the line
                (board_dimension, k * cell_dimension),           # the x/y coordinates of the endpoint of the line
                cell_line_width                          # the width (thickness) of the line (taken from TTT.gui)
            )

        for L in range(1, 9):           # make a for loop to make the necessary number of horizontal lines (8)
            pygame.draw.line(                   # designated function from pygame takes these parameters
                self.screen,                         # where it is being displayed
                line_color,                           # the color of the line (dark black)
                (L * cell_dimension, 0),               # the x/y coordinates of the startpoint of the line
                (L * cell_dimension, board_dimension),           # the x/y coordinates of the endpoint of the line
                cell_line_width                          # the width (thickness) of the line (taken from TTT.gui)
            )

    def select(self, row, col):
        pass

    def click(self, x, y):
        if 0 <= x <= self.width and 0 <= y <= self.height:     # if x and y are within the ranges of the board
            row, col = (y // cell_dimension), (x // cell_dimension)  # divide x and y by cell size to get the row/col
            return row, col

    def clear(self):
        Cell.set_sketched_value(self, 0)            # this should reference the set_sketched_value from the cell class
        # first parameter likely needs to be something else

    def sketch(self, value):
        Cell.set_sketched_value(self, value)  # this should reference the set_sketched_value from the cell class
        # first parameter likely needs to be something else
        # I believe I need to make a different draw function for drawing sketched values

    def place_number(self, value):
        pass            # i really don't know I feel like I'm doing all of this wrong

    def reset_to_original(self):
        pass

    def is_full(self):
        for num in SudokuGenerator.get_board():  # Uses get_board from SudokuGenerator to check if a cell has a value
            if num == 0:  # cell value is 0 if cell is empty
                return False
        return True  # returns true if all cells have value other than 0

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass


# pygame.init()       # initializes pygame
# pygame.display.set_caption("Group 9 Sudoku Game")           # sets caption of pygame
# screen = pygame.display.set_mode((675, 675))                # sets screen to equal pygame screen
# screen.fill((255, 255, 245))                                # fills with background color (white)
# board = Board(675, 675, screen, "easy")                     # initializes board inside Board class
# Board.draw(board)                                           # calls draw func which draws box lines on board
# pygame.display.update()                                     # updates screen


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         if event.type == pygame.MOUSEBUTTONDOWN:            # if the event is a mouseclick
#             x, y = event.pos                                # x and y are the coordinate position of the mouse click
#             row, col = Board.click(board, x, y)
#             current = SudokuGenerator.board[row][col]
