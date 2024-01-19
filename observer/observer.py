from abc import abstractmethod
from typing import List

from observer.constant import MessageType


class Observer: # TODO: Observer pattern
    def __init__(self):
        self._observers = []

    def listen_to(self, observer: type['Observer']):
        self._observers.append(observer)

    def disconnect_from(self, observer: type['Observer']):
        self._observers.remove(observer)

    def send(self, msg: type[MessageType]):
        for observer in self._observers:
            observer.on_message_received(msg)

    @abstractmethod
    def on_message_received(self, msg: type[MessageType]):
        pass