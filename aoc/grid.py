from collections.abc import Callable, Iterator
from functools import cache

__all__ = [
    "Grid",
    "GridPos",
]

type GridPos = tuple[int, int]


class Grid[T: str | int]:

    CARDINALS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    DIAGONALS = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    ADJACENTS = CARDINALS + DIAGONALS

    def __init__(
        self, rows: list[str],
        *, transformer: Callable[[str], T] | None = None,
    ) -> None:
        self.internal: list[list[T]] = [
            *map(
                lambda row:
                    [*map(transformer, row)] if transformer else [*row],  # pyright: ignore[reportUnknownLambdaType]
                [*map(str.strip, rows)],
            ),
        ]

    def __str__(self) -> str:
        string = f"    {' '.join(map(str, range(len(self.internal[0]))))}\n"
        for r_index, row in enumerate(self.internal):
            string += f"{r_index:3d} "
            for _, value in enumerate(row):
                string += f"{value} "
            string += "\n"
        return string

    def __getitem__(self, item: GridPos) -> T:
        return self.internal[item[0]][item[1]]

    def __setitem__(self, key: GridPos, value: T) -> None:
        self.internal[key[0]][key[1]] = value

    @cache
    def is_pos_valid(self, item: GridPos) -> bool:
        return (0 <= item[0] < len(self.internal)) and (0 <= item[1] < len(self.internal[0]))

    def positions(self) -> Iterator[GridPos]:
        for x in range(len(self.internal)):
            for y in range(len(self.internal[0])):
                yield x, y

    def values(self) -> Iterator[T]:
        for row in self.internal:
            for value in row:
                yield value

    def enumerate(self) -> Iterator[tuple[GridPos, T]]:
        for x, row in enumerate(self.internal):
            for y, value in enumerate(row):
                yield (x, y), value

    def find(self, value: T) -> GridPos:
        return [x for x in [*self.enumerate()] if x[-1] == value][0][0]

    def count(self, value: T) -> int:
        return str(self).count(str(value))
