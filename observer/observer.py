from typing import List, Type, Optional

import pygame

from observer.constant import MessageType
from observer.listener import Listener
from singleton import Singleton


class Observer(Singleton):  # TODO: Observer pattern
    _observers: List[Listener] = []

    def listen_to(self, listener: Listener):
        self._observers.append(listener)

    def disconnect_from(self, listener: Listener):
        self._observers.remove(listener)

    def send(self, msg: Type[MessageType], selected_indexes: Optional[List[int]] = None, **kwargs):
        for observer in self._observers:
            observer.on_message_received(msg, selected_squares=selected_indexes, **kwargs)
