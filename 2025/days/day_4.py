from aoc import Day
from aoc.grid import Grid


class Day4(Day[Grid[str]]):

    def parse(self):
        return Grid[str](self.LINES)

    def part_one(self):
        found = set[tuple[int, int]]()
        for (x, y), cell in self.INPUT.enumerate():
            if cell == "@" and sum(
                1 for (x_offset, y_offset) in self.INPUT.ADJACENTS
                if self.INPUT.is_pos_valid(pos := (x + x_offset, y + y_offset)) and self.INPUT[pos] == "@"
            ) < 4:
                found.add((x, y))
        return len(found)

    def part_two(self):
        removed = set[tuple[int, int]]()
        while True:
            done = False
            for (x, y), cell in self.INPUT.enumerate():
                if cell == "@" and sum(
                    1 for (x_offset, y_offset) in self.INPUT.ADJACENTS
                    if self.INPUT.is_pos_valid(pos := (x + x_offset, y + y_offset)) and self.INPUT[pos] == "@"
                ) < 4:
                    removed.add((x, y))
                    self.INPUT[(x, y)] = "x"
                    done = True
            if not done:
                break
        return len(removed)


day = Day4()
day.run(day.part_one, day.part_two)
