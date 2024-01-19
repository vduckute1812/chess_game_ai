from pieces.contants import PieceType

ASSETS_DIR = 'assets/pieces/'

BOARD_CONFIG = {
    PieceType.W_ROOK:   [0, 7],
    PieceType.W_KNIGHT: [1, 6],
    PieceType.W_BISHOP: [2, 5],
    PieceType.W_KING:   [3],
    PieceType.W_QUEEN:  [4],
    PieceType.W_PAWN:   [8, 9, 10, 11, 12, 13, 14, 15],
    PieceType.B_PAWN:   [48, 49, 50, 51, 52, 53, 54, 55],
    PieceType.B_KING:   [59],
    PieceType.B_QUEEN:  [60],
    PieceType.B_BISHOP: [58, 61],
    PieceType.B_KNIGHT: [57, 62],
    PieceType.B_ROOK:   [56, 63],
}

