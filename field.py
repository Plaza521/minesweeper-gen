import typing as tp
from random import randint
import cell


class Field:
    def __init__(
        self,
        field_size: int,
        mines_amount: int
    ) -> None:
        self.field_size: int = field_size
        self.mines_around: int = mines_amount
        self.field: tp.List[tp.List[cell.Cell]]

    def generate(
        self
    ) -> None:
        self.field = \
            [[cell.Cell] * self.field_size for _ in range(self.field_size)]
        mines_left = self.mines_amount
        while mines_left:
            x = randint(self.field_size - 1)
            y = randint(self.field_size - 1)
            if self.field[y][x].is_mine:
                mines_left += 1
                continue
            for i in range(-1, 2):
                for j in range(-1, 2):
                    rx = x + i
                    ry = y + j
                    if rx < 0 or ry < 0 or \
                       rx > self.field_size or ry > self.field_size:
                        continue
                    self.field[y][x].mines_around += 1
