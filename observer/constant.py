class MessageType:
    INIT_BOARD = 0
    BOARD_CHANGED = 1
    MOVE_MADE = 2
    GAME_OVER = 3
    LOCK_BOARD = 4
    SQUARE_HIGHLIGHT = 5

    @classmethod
    def is_move_made(cls, msg_type: int):
        return msg_type == cls.MOVE_MADE

    @classmethod
    def is_board_change(cls, msg_type: int):
        return msg_type == cls.BOARD_CHANGED

    @classmethod
    def is_init_board(cls, msg_type: int):
        return msg_type == cls.INIT_BOARD

    @classmethod
    def is_square_highlight(cls, msg_type: int):
        return msg_type == cls.SQUARE_HIGHLIGHT
