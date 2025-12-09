import itertools

from shapely import MultiPoint
from shapely.geometry.polygon import Polygon

from aoc import Day


class Day9(Day[list[tuple[int, int]]]):

    def parse(self) -> list[tuple[int, int]]:
        return [*map(lambda line: tuple[int, int](map(int, line.split(","))), self.LINES)]

    def part_one(self) -> int:
        return sorted(
            map(
                lambda x: (abs(x[0][0] - x[1][0]) + 1) * (abs(x[0][1] - x[1][1]) + 1),
                itertools.combinations(self.input, 2),
            ),
            reverse=True,
        )[0]

    def part_two(self) -> int:
        polygon = Polygon(self.input)
        biggest = 0
        for combo in itertools.combinations(self.input, 2):
            if not polygon.contains(
                MultiPoint([*combo, (combo[1][0], combo[0][1]), (combo[0][0], combo[1][1])]).convex_hull,
            ):
                continue
            biggest = max(
                biggest,
                (abs(combo[0][0] - combo[1][0]) + 1) * (abs(combo[0][1] - combo[1][1]) + 1)
            )
        return biggest


day = Day9()
day.run(day.part_one, day.part_two)
