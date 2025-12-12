import math

from aoc import Day


class Day12(Day[None]):

    def parse(self) -> None:
        return None

    def part_one(self) -> int:
        groups: list[str] = self.TEXT.split("\n\n")
        present_sizes: list[int] = list(map(
            lambda present: present.count("#"),
            groups[:-1],
        ))
        trees: list[tuple[list[int], list[int]]] = list(map(
            lambda part: (
                list(map(int, part[0].split("x"))),
                list(map(int, part[1].split(" "))),
            ),
            map(
                lambda line: line.split(": "),
                groups[-1].split("\n"),
            ),
        ))
        return sum([
            1 for (x, y), present_counts in trees
            if (
                sum(map(math.prod, zip(present_sizes, present_counts))) <= (x * y)
                and
                sum(present_counts) <= (x // 3) * (y // 3)
            )
        ])


day = Day12()
day.run(day.part_one)
