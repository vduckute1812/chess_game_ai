class PieceTypeValues:
    PAWN = 100
    KNIGHT = 320
    BISHOP = 330
    ROOK = 500
    QUEEN = 900
    KING = 20000


class PieceType:
    UNKNOWN = 0
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    KING = 5
    QUEEN = 6


PIECE_TYPE_MAP = {
    "P": PieceType.PAWN,
    "B": PieceType.BISHOP,
    "R": PieceType.ROOK,
    "K": PieceType.KNIGHT,
    "Q": PieceType.QUEEN,
    "Z": PieceType.KING,
}


class Alliance:
    WHITE = 1
    BLACK = 2

    @classmethod
    def to_notation(cls, val: int) -> str:
        return 'w' if cls.is_white(val) else 'b'

    @classmethod
    def to_value(cls, val: str) -> int:
        return Alliance.WHITE if val == 'w' else Alliance.BLACK

    @classmethod
    def is_black(cls, val) -> bool:
        return cls.BLACK == val

    @classmethod
    def is_white(cls, val) -> bool:
        return cls.WHITE == val

