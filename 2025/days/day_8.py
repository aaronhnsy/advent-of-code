import itertools
import math
from typing import NamedTuple

from aoc import Day

type Pair = tuple[Junction, Junction]


class Junction(NamedTuple):
    x: int
    y: int
    z: int


class Day8(Day[list[Junction]]):

    def __init__(self) -> None:
        super().__init__()
        self.pairs: list[Pair] = sorted(
            itertools.combinations(self.input, 2),
            key=lambda pair:
                math.sqrt(
                    (abs(pair[1].x - pair[0].x) ** 2) +
                    (abs(pair[1].y - pair[0].y) ** 2) +
                    (abs(pair[1].z - pair[0].z) ** 2),
                ),
        )
        self.connections: list[list[Junction]] = [[junction] for junction in self.input]

    def parse(self) -> list[Junction]:
        return [Junction(*map(int, line.split(","))) for line in self.LINES]

    def part_one(self) -> int:
        for junction_one, junction_two in self.pairs[:999]:
            junction_one_idx = self.connections.index([c for c in self.connections if junction_one in c][0])
            junction_two_idx = self.connections.index([c for c in self.connections if junction_two in c][0])
            if junction_one_idx == junction_two_idx:
                continue
            self.connections[junction_one_idx].extend(self.connections[junction_two_idx])
            self.connections.pop(junction_two_idx)
        return math.prod(map(len, sorted(self.connections, key=len, reverse=True)[:3]))

    def part_two(self) -> int:
        last: Pair | None = None
        while len(self.connections) != 1:
            last = self.pairs.pop(0)
            junction_one, junction_two = last
            junction_one_idx = self.connections.index([c for c in self.connections if junction_one in c][0])
            junction_two_idx = self.connections.index([c for c in self.connections if junction_two in c][0])
            if junction_one_idx == junction_two_idx:
                continue
            self.connections[junction_one_idx].extend(self.connections[junction_two_idx])
            self.connections.pop(junction_two_idx)
        return last[0].x * last[1].x if last else -1


day = Day8()
day.run(day.part_one, day.part_two)
