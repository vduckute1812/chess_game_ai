from boards.constant import Alliance


class PieceType:
    UNKNOWN = 0
    W_PAWN = 1
    W_KNIGHT = 2
    W_BISHOP = 3
    W_ROOK = 4
    W_QUEEN = 5
    W_KING = 6
    B_PAWN = 7
    B_KNIGHT = 8
    B_BISHOP = 9
    B_ROOK = 10
    B_QUEEN = 11
    B_KING = 12

    @classmethod
    def is_black(cls, piece_type: int) -> bool:
        return piece_type in [cls.B_KING, cls.B_PAWN, cls.B_KNIGHT, cls.B_BISHOP, cls.B_ROOK, cls.B_QUEEN]

    @classmethod
    def is_white(cls, piece_type: int) -> bool:
        return piece_type in [cls.W_KING, cls.W_PAWN, cls.W_KNIGHT, cls.W_BISHOP, cls.W_ROOK, cls.W_QUEEN]

    @classmethod
    def is_king(cls, piece_type: int) -> bool:
        return piece_type in [cls.W_KING, cls.B_KING]

    @classmethod
    def is_queen(cls, piece_type: int) -> bool:
        return piece_type in [cls.W_QUEEN, cls.B_QUEEN]

    @classmethod
    def is_bishop(cls, piece_type: int) -> bool:
        return piece_type in [cls.W_BISHOP, cls.B_BISHOP]

    @classmethod
    def is_rook(cls, piece_type: int) -> bool:
        return piece_type in [cls.W_ROOK, cls.B_ROOK]

    @classmethod
    def is_knight(cls, piece_type: int) -> bool:
        return piece_type in [cls.W_KNIGHT, cls.B_KNIGHT]

    @classmethod
    def is_pawn(cls, piece_type: int) -> bool:
        return piece_type in [cls.W_PAWN, cls.B_PAWN]

    @classmethod
    def to_str(cls, piece_type: int) -> str:
        """
        Piece type to string. 14 -> 'b_king'
        :param piece_type:
        :return:
        """
        allience = "w" if cls.is_white(piece_type) else "b"
        piece_key = 'king' if cls.is_king(piece_type) else \
            'queen' if cls.is_queen(piece_type) else \
                'bishop' if cls.is_bishop(piece_type) else \
                    'rook' if cls.is_rook(piece_type) else \
                        'knight' if cls.is_knight(piece_type) else \
                            'pawn'
        return allience + "_" + piece_key

    @classmethod
    def list_all(cls):
        return [cls.W_PAWN, cls.W_KNIGHT, cls.W_BISHOP, cls.W_ROOK, cls.W_QUEEN, cls.W_KING,
                cls.B_PAWN, cls.B_KNIGHT, cls.B_BISHOP, cls.B_ROOK, cls.B_QUEEN, cls.B_KING]

    @classmethod
    def get_alliance(cls, piece_type):
        return Alliance.WHITE if cls.is_white(piece_type) else Alliance.BLACK
