import itertools
import pathlib

from aoc import Day


class Day2(Day[list[str]]):

    def parse(self):
        return pathlib.Path(self.FILE).read_text().split(sep=",")

    def part_one(self):
        total = 0
        for ids in self.INPUT:
            first, second = map(int, ids.split(sep="-"))
            for id_int in range(first, second + 1):
                id_str = [*str(id_int)]
                length = len(id_str)
                if length % 2 == 0 and id_str[length // 2:] == id_str[:length // 2]:
                    total += id_int
        return total

    def part_two(self):
        total = 0
        for ids in self.INPUT:
            first, second = map(int, ids.split(sep="-"))
            for id_int in range(first, second + 1):
                id_str = [*str(id_int)]
                for window in range(1, len(id_str) + 1):
                    checks = list(
                        id_str[:window] == [*batch] for batch
                        in itertools.batched(id_str[window:], window)
                    )
                    if len(checks) != 0 and all(checks):
                        total += id_int
                        break
        return total


day = Day2()
day.run(day.part_one, day.part_two)
