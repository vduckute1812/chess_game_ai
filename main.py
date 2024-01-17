import pygame
from boards.board import Board
from boards.constant import WINDOW_SIZE
from controller.board_controller import BoardController
from events.event_processor import EventProcessor


def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board = Board()
    controller = BoardController(board)
    event_processor = EventProcessor()
    while controller.is_running():
        event_processor.process(controller)
        draw(screen)