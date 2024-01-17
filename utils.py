from typing import TYPE_CHECKING, Type, Tuple
import pygame
from boards.constant import BOARD_COLUMNS, WINDOW_SIZE
from constant import ASSETS_DIR
from pieces.contants import PIECE_TYPE_MAP, Alliance, PieceType
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.rook import Rook

if TYPE_CHECKING:
    from boards.board import Board



class Utils:
    PIECE_TYPE_OBJ_MAP = {
        PieceType.PAWN: Pawn,
        PieceType.BISHOP: Bishop,
        PieceType.ROOK: Rook,
        PieceType.KNIGHT: Knight,
        PieceType.QUEEN: Queen,
        PieceType.KING: King,
    }

    @classmethod
    def generate_piece_by_key(cls, piece_key: str) -> Tuple[Type[Piece], int]:
        alliance_notation, piece_type_str = piece_key[0], piece_key[1]
        piece_type = PIECE_TYPE_MAP.get(piece_type_str)
        alliance = Alliance.to_value(alliance_notation)
        return cls.PIECE_TYPE_OBJ_MAP.get(piece_type, Piece), alliance

    @classmethod
    def generate_piece_img(cls, piece_type: int, alliance: int):
        tile_width, tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        piece_type = {v: k for k, v in PIECE_TYPE_MAP.items()}.get(piece_type, "")
        if piece_type:
            img_path = ASSETS_DIR + Alliance.to_notation(alliance) + '_' + piece_type + '.png'
            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (tile_width - 35, tile_height - 35))
            return img

    @classmethod
    def set_init_board(cls, board: "Board"):    # Factory method
        init_config = {
            "wR": "a1 h1",
            "wK": "b1 g1",
            "wB": "c1 f1",
            "wZ": "d1",
            "wQ": "e1",
            "wP": "a2 b2 c2 d2 e2 f2 g2 h2",
            "bP": "a7 b7 c7 d7 e7 f7 g7 h7",
            "bZ": "d8",
            "bQ": "e8",
            "bB": "c8 f8",
            "bK": "b8 g8",
            "bR": "a8 h8",
        }
        tiles = board.get_board_tiles()
        for piece_key, positions in init_config.items():
            piece_cls, alliance = cls.generate_piece_by_key(piece_key)
            for position in positions.split(" "):
                row, col = int(position[1]) - 1, BOARD_COLUMNS.index(position[0])
                piece_obj = piece_cls(alliance)
                piece_obj.set_square_index(row * 8 + col)
                tiles[row][col].set_piece(piece_obj)

    @classmethod
    def coord_to_position(cls, mx: int, my: int) -> Tuple[int, int]:
        tile_width, tile_height = WINDOW_SIZE[0] // 8, WINDOW_SIZE[1] // 8
        col = mx // tile_width
        row = my // tile_height
        return row, col

    @classmethod
    def position_to_index(cls, row: int, col: int) -> int:
        return row * 8 + col