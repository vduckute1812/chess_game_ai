class MoveType:
    NORMAL = 1
    ATTACK = 2
    PROMOTE = 3
    CASTLE = 4

    @classmethod
    def is_normal(cls, move_type: int) -> bool:
        return move_type == cls.NORMAL

    @classmethod
    def is_attack(cls, move_type: int) -> bool:
        return move_type == cls.ATTACK
