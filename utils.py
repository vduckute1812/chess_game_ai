from enum import Enum
from typing import Type, Tuple, List, Dict
import pygame
from boards.constant import WINDOW_SIZE
from boards.square import Square
from constant import ASSETS_DIR, BOARD_CONFIG
from pieces.contants import PieceType
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.rook import Rook



class Utils:

    @classmethod
    def generate_piece_cls(cls, piece_type: str) -> Type[Piece]:
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
    def generate_piece_img_map(cls) -> Dict[Enum, pygame.Surface]:
        tile_width, tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        piece_img_map = {}
        for piece_type in PieceType.list_all():
            piece_str = PieceType.to_str(piece_type)
            if piece_type and piece_type not in piece_img_map:
                img_path = ASSETS_DIR + piece_str + '.png'
                img = pygame.image.load(img_path)
                img = pygame.transform.scale(img, (tile_width - 35, tile_height - 35))
                piece_img_map[piece_type] = img
        return piece_img_map

    @classmethod
    def generate_squares(cls) -> List[Square]:
        tiles = []
        tile_width, tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        for row in range(8):
            for col in range(8):
                tiles.append(Square(row * 8 + col, tile_width, tile_height))
        return tiles

    @classmethod
    def set_init_board(cls) -> List[Square]:  # Factory method
        squares = cls.generate_squares()
        piece_img_map = cls.generate_piece_img_map()
        for piece_type, positions in BOARD_CONFIG.items():
            img = piece_img_map.get(piece_type)
            piece_cls = cls.generate_piece_cls(piece_type)
            for index in positions:
                piece_obj = piece_cls(square_index=index, piece_type=piece_type, img=img)
                squares[index].set_piece(piece_obj)
        return squares

    @classmethod
    def coord_to_position(cls, mx: int, my: int) -> Tuple[int, int]:
        tile_width, tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        col = mx // tile_width
        row = my // tile_height
        return row, col
