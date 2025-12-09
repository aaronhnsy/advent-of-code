from collections.abc import Callable, Iterator
from functools import cache

__all__ = [
    "Grid",
    "Position",
    "NORTH",
    "NORTH_EAST",
    "EAST",
    "SOUTH_EAST",
    "SOUTH",
    "SOUTH_WEST",
    "WEST",
    "NORTH_WEST",
    "UP",
    "UP_RIGHT",
    "RIGHT",
    "DOWN_RIGHT",
    "DOWN",
    "DOWN_LEFT",
    "LEFT",
    "UP_LEFT",
    "CARDINALS",
    "ORDINALS",
    "ADJACENTS",
]


class Position:
    __slots__ = ("x", "y",)

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __add__(self, other: object) -> Position:
        if not isinstance(other, Position):
            return NotImplemented
        return Position(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: object) -> Position:
        if not isinstance(other, Position):
            return NotImplemented
        return self.__add__(other)

    def __sub__(self, other: object) -> Position:
        if not isinstance(other, Position):
            return NotImplemented
        return Position(self.x - other.x, self.y - other.y)

    def __isub__(self, other: object) -> Position:
        if not isinstance(other, Position):
            return NotImplemented
        return self.__sub__(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def is_valid(self, grid: Grid) -> bool:
        return grid.is_position_valid(self)


class Grid[T: str | int = str]:
    __slots__ = ("internal", "width", "height",)

    def __init__(
        self,
        rows: list[str], /,
        *, transformer: Callable[[str], T] | None = None,
    ) -> None:
        self.internal: list[list[T]] = [
            *map(
                lambda row: [*map(transformer, row)] if transformer else [*row],  # pyright: ignore
                [*map(str.strip, rows)],
            ),
        ]
        self.width = len(self.internal[0])
        self.height = len(self.internal)

    # dunder methods
    def __str__(self) -> str:
        string = f"    {' '.join(map(str, range(len(self.internal[0]))))}\n"
        for r_index, row in enumerate(self.internal):
            string += f"{r_index:3d} "
            for _, value in enumerate(row):
                string += f"{value} "
            string += "\n"
        return string

    def __getitem__(self, position: Position) -> T:
        return self.internal[position.y][position.x]

    def __setitem__(self, position: Position, value: T) -> None:
        self.internal[position.y][position.x] = value

    # methods
    @cache
    def is_position_valid(self, position: Position) -> bool:
        return (0 <= position.x < self.width) and (0 <= position.y < self.height)

    def positions(self) -> Iterator[Position]:
        for y in range(len(self.internal)):
            for x in range(len(self.internal[0])):
                yield Position(x, y)

    def values(self) -> Iterator[T]:
        for row in self.internal:
            for value in row:
                yield value

    def enumerate(self) -> Iterator[tuple[Position, T]]:
        for y, row in enumerate(self.internal):
            for x, value in enumerate(row):
                yield Position(x, y), value

    def find(self, value: T) -> Position:
        result = next(
            filter(lambda x: x[-1] == value, self.enumerate()),
            None,
        )
        if result is None:
            raise ValueError(f"'{value}' not found in grid.")
        return result[0]

    def count(self, value: T) -> int:
        return len(list(filter(lambda x: x == value, self.values())))


NORTH: Position = Position(0, -1)
UP: Position = NORTH

NORTH_EAST: Position = Position(1, -1)
UP_RIGHT: Position = NORTH_EAST

EAST: Position = Position(1, 0)
RIGHT: Position = EAST

SOUTH_EAST: Position = Position(1, 1)
DOWN_RIGHT: Position = SOUTH_EAST

SOUTH: Position = Position(0, 1)
DOWN: Position = SOUTH

SOUTH_WEST: Position = Position(-1, 1)
DOWN_LEFT: Position = SOUTH_WEST

WEST: Position = Position(-1, 0)
LEFT: Position = WEST

NORTH_WEST: Position = Position(-1, -1)
UP_LEFT: Position = NORTH_WEST

CARDINALS: tuple[Position, ...] = (NORTH, EAST, SOUTH, WEST)
ORDINALS: tuple[Position, ...] = (NORTH_WEST, NORTH_EAST, SOUTH_EAST, SOUTH_WEST)
ADJACENTS: tuple[Position, ...] = (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST)
