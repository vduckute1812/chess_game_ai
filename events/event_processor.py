from typing import List

import pygame

from controller.board_controller import BoardController
from events.base import BaseEvent
from events.constant import EventHandlerType
from events.game_event import GameEvent
from events.mouse_event import MouseEvent


class EventProcessor(BaseEvent):  # TODO: Composite pattern
    def __init__(self, _type: int = EventHandlerType.UNKNOWN):
        super().__init__(_type)
        self._events: List[BaseEvent] = []

    def add(self, event: BaseEvent):
        self._events.append(event)

    def collect_events(self):
        # Process the event
        for event in pygame.event.get():
            if self.is_quit(event):
                self.add(GameEvent(EventHandlerType.QUIT))
            elif self.is_click(event):
                self.add(MouseEvent(EventHandlerType.MOUSE_CLICK, event.pos))

    def process(self, controller):
        self.collect_events()
        while self._events:
            event = self._events.pop(0) # FIFO
            event.process(controller)

    @staticmethod
    def is_quit(event) -> bool:
        return event.type == pygame.QUIT or event.type == pygame.TEXTINPUT and event.text == 'q'

    @staticmethod
    def is_click(event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1