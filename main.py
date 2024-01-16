import pygame

from boards.board import Board
from boards.constant import WINDOW_SIZE
from controller.board_controller import BoardController
from pieces.contants import Alliance
from pieces.pawn import Pawn


def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board = Board()
    controller = BoardController(board)
    running = True
    while running:
        draw(screen)