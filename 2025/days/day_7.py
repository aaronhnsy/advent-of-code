from functools import lru_cache

from aoc import Day, EAST, Grid, SOUTH, WEST
from aoc.grid import Position


class Day7(Day[Grid[str]]):

    def parse(self) -> Grid[str]:
        return Grid[str](self.LINES)

    def part_one(self) -> int:
        self.input[self.input.find("S") + SOUTH] = "|"
        count = 0
        for position, cell in self.input.enumerate():
            down = position + SOUTH
            if cell != "|" or not down.is_valid(self.input):
                continue
            match self.input[down]:
                case "^":
                    self.input[down + WEST] = "|"
                    self.input[down + EAST] = "|"
                    count += 1
                case ".":
                    self.input[down] = "|"
                case _:
                    continue
        return count

    def part_two(self) -> int:
        @lru_cache(maxsize=None)
        def recurse(position: Position) -> int:
            position += SOUTH
            while position.is_valid(self.input) and self.input[position] != "^":
                position += SOUTH
            if not position.is_valid(self.input):
                return 1
            return recurse(position + WEST) + recurse(position + EAST)

        return recurse(self.input.find("S"))


day = Day7()
day.run(day.part_one, day.part_two)
