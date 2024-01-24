from boards.pieces.contants import PieceType

ASSETS_DIR = 'assets/pieces/'

BOARD_CONFIG = {
    PieceType.B_ROOK:   [0, 7],
    PieceType.B_KNIGHT: [1, 6],
    PieceType.B_BISHOP: [2, 5],
    PieceType.B_KING:   [3],
    PieceType.B_QUEEN:  [4],
    PieceType.B_PAWN:   [8, 9, 10, 11, 12, 13, 14, 15],
    PieceType.W_PAWN:   [48, 49, 50, 51, 52, 53, 54, 55],
    PieceType.W_KING:   [59],
    PieceType.W_QUEEN:  [60],
    PieceType.W_BISHOP: [58, 61],
    PieceType.W_KNIGHT: [57, 62],
    PieceType.W_ROOK:   [56, 63],
}

