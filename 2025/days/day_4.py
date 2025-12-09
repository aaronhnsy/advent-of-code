from aoc import Day
from aoc.grid import Grid, ADJACENTS


class Day4(Day[Grid[str]]):

    def parse(self) -> Grid[str]:
        return Grid[str](self.LINES)

    def part_one(self) -> int:
        count = 0
        for position, value in self.input.enumerate():
            if value == "@" and sum(
                1 for offset in ADJACENTS
                if (pos := position + offset).is_valid(self.input) and self.input[pos] == "@"
            ) < 4:
                count += 1
        return count

    def part_two(self) -> int:
        count = 0
        while True:
            removed = False
            for position, value in self.input.enumerate():
                if value == "@" and sum(
                    1 for offset in ADJACENTS
                    if (pos := position + offset).is_valid(self.input) and self.input[pos] == "@"
                ) < 4:
                    count += 1
                    self.input[position] = "x"
                    removed = True
            if not removed:
                break
        return count


day = Day4()
day.run(day.part_one, day.part_two)
