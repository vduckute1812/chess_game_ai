from enum import Enum
from typing import Type, Tuple, List, Dict
import pygame
from boards.constant import WINDOW_SIZE
from boards.square import Square
from boards.pieces.contants import PieceType
from boards.pieces.bishop import Bishop
from boards.pieces.king import King
from boards.pieces.knight import Knight
from boards.pieces.pawn import Pawn
from boards.pieces.piece import Piece
from boards.pieces.queen import Queen
from boards.pieces.rook import Rook


ASSETS_DIR = 'assets/pieces/'

class Utils:

    @classmethod
    def generate_piece_cls(cls, piece_type: int) -> Type[Piece]:
        match piece_type:
            case PieceType.W_PAWN | PieceType.B_PAWN:
                return Pawn
            case PieceType.W_KNIGHT | PieceType.B_KNIGHT:
                return Knight
            case PieceType.W_BISHOP | PieceType.B_BISHOP:
                return Bishop
            case PieceType.W_ROOK | PieceType.B_ROOK:
                return Rook
            case PieceType.W_QUEEN | PieceType.B_QUEEN:
                return Queen
            case PieceType.W_KING | PieceType.B_KING:
                return King
            case _:
                return Piece

    @classmethod
    def generate_new_piece(cls, piece_type: int, square_index: int) -> Piece:
        img = cls.generate_piece_img(piece_type=piece_type)
        piece_cls = cls.generate_piece_cls(piece_type)
        return piece_cls(piece_type=piece_type, img=img, square_index=square_index)

    @classmethod
    def generate_piece_img(cls, piece_type: int) -> pygame.Surface:
        piece_str = PieceType.to_str(piece_type)
        img_path = ASSETS_DIR + piece_str + '.png'
        img = pygame.image.load(img_path)
        tile_width, tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        img = pygame.transform.scale(img, (tile_width - 35, tile_height - 35))
        return img

    @classmethod
    def generate_squares(cls) -> List[Square]:
        tiles = []
        tile_width, tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        for row in range(8):
            for col in range(8):
                tiles.append(Square(row * 8 + col, tile_width, tile_height))
        return tiles

    @classmethod
    def set_init_board(cls, board_config: Dict) -> List[Square]:  # Factory method
        squares = cls.generate_squares()
        for piece_type, positions in board_config.items():
            for square_index in positions:
                piece_obj = cls.generate_new_piece(piece_type, square_index)
                squares[square_index].set_piece(piece_obj)
        return squares

    @classmethod
    def coord_to_position(cls, mx: int, my: int) -> Tuple[int, int]:
        tile_width, tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        col = mx // tile_width
        row = my // tile_height
        return row, col
