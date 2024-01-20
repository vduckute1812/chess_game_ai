class Color:
    WHITE = 1
    BLACK = 2


SQUARE_COLOR_MAP = {
    Color.WHITE: (220, 208, 194),
    Color.BLACK: (53, 53, 53),
}

HIGH_LIGHT_SQUARE_COLOR_MAP = {
    Color.WHITE: (100, 249, 83),
    Color.BLACK: (0, 228, 10),
}

ATTACK_SQUARE_COLOR_MAP = {
    Color.WHITE: (255, 51, 133),
    Color.BLACK: (255, 0, 102),
}

WINDOW_SIZE = (600, 600)


class Alliance:
    WHITE = 0
    BLACK = 1
    BOTH = 2

    @classmethod
    def is_black(cls, alliance: int) -> bool:
        return alliance == cls.BLACK

    @classmethod
    def is_white(cls, alliance: int) -> bool:
        return alliance == cls.WHITE

    @classmethod
    def is_same(cls, alliance1: int, alliance2: int) -> bool:
        return alliance1 == alliance2

    @classmethod
    def is_opposite(cls, alliance1: int, alliance2: int) -> bool:
        return not cls.is_same(alliance1, alliance2)
