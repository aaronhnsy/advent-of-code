import itertools

from aoc import Day


class Day2(Day[list[str]]):

    def parse(self) -> list[str]:
        return self.TEXT.split(",")

    def part_one(self) -> int:
        total = 0
        for ids in self.input:
            start, end = map(int, ids.split(sep="-"))
            for id_int in range(start, end + 1):
                id_str = list(str(id_int))
                length = len(id_str)
                if length % 2 == 0 and id_str[length // 2:] == id_str[:length // 2]:
                    total += id_int
        return total

    def part_two(self) -> int:
        total = 0
        for ids in self.input:
            start, end = map(int, ids.split(sep="-"))
            for id_int in range(start, end + 1):
                id_str = list(str(id_int))
                for window in range(1, len(id_str) + 1):
                    if len(checks := list(
                        id_str[:window] == [*batch]
                        for batch in itertools.batched(id_str[window:], window)
                    )) != 0 and all(checks):
                        total += id_int
                        break
        return total


day = Day2()
day.run(day.part_one, day.part_two)
