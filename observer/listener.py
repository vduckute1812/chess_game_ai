from abc import ABC, abstractmethod
from typing import Type

from observer.constant import MessageType


class Listener(ABC):

    @classmethod
    @abstractmethod
    def on_message_received(cls, msg: Type[MessageType]):
        pass
