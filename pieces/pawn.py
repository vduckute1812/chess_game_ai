from typing import Tuple

import pygame

from boards.square import Square
from pieces.contants import Alliance
from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, alliance: int):
        super().__init__(alliance)
        img_path = 'assets/pieces/' + Alliance.to_notation(alliance) + '_pawn.png'
        self._img = pygame.image.load(img_path)
        self._img = pygame.transform.scale(self._img, (self._tile_width - 35, self._tile_height - 35))
