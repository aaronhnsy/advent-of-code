import math
import itertools

from aoc import Day


class Day6(Day[list[str]]):

    def parse(self) -> list[str]:
        return self.LINES

    def part_one(self):
        return sum(
            map(
                lambda problem: (sum if problem.pop() == "+" else math.prod)(map(int, problem)),
                map(list, zip(*[*map(str.split, self.input)])),
            )
        )

    def part_two(self):
        operations = self.input.pop().split()
        width = max(map(len, self.input))
        lines = [*map(lambda line: line.ljust(width), self.input)]
        columns = map(lambda column: "".join(row[column].strip() for row in lines), range(width))
        return sum(
            map(
                lambda problem: (sum if operations[problem[0]] == "+" else math.prod)(map(int, problem[1][1])),
                enumerate(filter(lambda x: x[0], itertools.groupby(columns, "".__ne__))),
            )
        )


day = Day6()
day.run(day.part_one, day.part_two)
