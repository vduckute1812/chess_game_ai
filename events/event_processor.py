from typing import List

import pygame
from events.base import BaseEvent
from events.constant import EventHandlerType
from events.event_handler import EventHandler


class EventProcessor(BaseEvent):  # TODO: Composite pattern
    def __init__(self):
        super().__init__()
        self._events: List[BaseEvent] = []

    def add(self, event: BaseEvent):
        self._events.append(event)

    def collect_events(self):
        # Process the event
        for event in pygame.event.get():
            if self.is_quit(event):
                self.add(EventHandler(EventHandlerType.QUIT))
            elif self.is_click(event):
                self.add(EventHandler(EventHandlerType.MOUSE_CLICK, event.pos))
            elif self.is_undo(event):
                self.add(EventHandler(EventHandlerType.UNDO))
            elif self.is_redo(event):
                self.add(EventHandler(EventHandlerType.REDO))

    def process(self):
        self.collect_events()
        while self._events:
            event = self._events.pop(0) # FIFO
            event.process()

    @staticmethod
    def is_quit(event) -> bool:
        return event.type == pygame.QUIT or event.type == pygame.TEXTINPUT and event.text == 'q'

    @staticmethod
    def is_click(event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

    @staticmethod
    def is_undo(event):
        return event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT

    @staticmethod
    def is_redo(event):
        return event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT
