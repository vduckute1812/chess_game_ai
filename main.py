import pygame

from boards.board import Board
from boards.constant import WINDOW_SIZE
from controller.board_controller import BoardController
from events.event_processor import EventProcessor

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    controller = BoardController()
    board = controller.get_board()
    event_processor = EventProcessor()
    while controller.is_running():
        event_processor.process()
        board.draw(screen)
