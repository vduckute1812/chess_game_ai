from pieces.contants import PieceType


PIECE_VALUE_MAP = {
    PieceType.W_PAWN: 1,
    PieceType.W_KNIGHT: 3,
    PieceType.W_BISHOP: 3,
    PieceType.W_ROOK: 5,
    PieceType.W_QUEEN: 9,
    PieceType.W_KING: 99,
    PieceType.B_PAWN: -1,
    PieceType.B_KNIGHT: -3,
    PieceType.B_BISHOP: -3,
    PieceType.B_ROOK: -5,
    PieceType.B_QUEEN: -9,
    PieceType.B_KING: -99
}


KNIGHT_SCORES = [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0,
                 0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1,
                 0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2,
                 0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2,
                 0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2,
                 0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2,
                 0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1,
                 0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]

BISHOP_SCORES = [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0,
                 0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2,
                 0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2,
                 0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2,
                 0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2,
                 0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2,
                 0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2,
                 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]

ROOK_SCORES = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
               0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]

QUEEN_SCORES = [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0,
                0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2,
                0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2,
                0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3,
                0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3,
                0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2,
                0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2,
                0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]

PAWN_SCORES = [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
               0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7,
               0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3,
               0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25,
               0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2,
               0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25,
               0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25,
               0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

PIECE_POSITION_SCORES = {
    PieceType.W_KNIGHT: KNIGHT_SCORES,
    PieceType.B_KNIGHT: KNIGHT_SCORES[::-1],
    PieceType.W_BISHOP: BISHOP_SCORES,
    PieceType.B_BISHOP: BISHOP_SCORES[::-1],
    PieceType.W_ROOK: ROOK_SCORES,
    PieceType.B_ROOK: ROOK_SCORES[::-1],
    PieceType.W_QUEEN: QUEEN_SCORES,
    PieceType.B_QUEEN: QUEEN_SCORES[::-1],
    PieceType.W_PAWN: PAWN_SCORES,
    PieceType.B_PAWN: PAWN_SCORES[::-1]
}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3