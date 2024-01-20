import pygame

from boards.board import Board
from controller.board_controller import BoardController
from events.event_processor import EventProcessor

if __name__ == '__main__':
    pygame.init()
    controller = BoardController()
    controller.set_board(board=Board())
    event_processor = EventProcessor()
    while controller.is_running():
        event_processor.process()
