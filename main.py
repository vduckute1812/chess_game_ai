import pygame

from boards.board import Board
from controller.board_controller import BoardController
from events.event_processor import EventProcessor
from ai_engine.minimax.minimax import Minimax

if __name__ == '__main__':
    pygame.init()
    controller = BoardController()
    controller.set_board(board=Board())
    event_processor = EventProcessor()
    minimax = Minimax()
    while controller.is_running():
        event_processor.process()
