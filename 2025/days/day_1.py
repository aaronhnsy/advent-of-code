from aoc import Day


class Day1(Day[list[tuple[str, int]]]):

    def parse(self) -> list[tuple[str, int]]:
        return [(line[0], int(line[1:])) for line in self.LINES]

    def part_one(self) -> int:
        position = 50
        count = 0
        for direction, distance in self.input:
            if direction == "L":
                for _ in range(distance):
                    position += 1
                    if position > 99:
                        position = 0
            elif direction == "R":
                for _ in range(distance):
                    position -= 1
                    if position < 0:
                        position = 99
            if position == 0:
                count += 1
        return count

    def part_two(self) -> int:
        position = 50
        count = 0
        for direction, distance in self.input:
            if direction == "L":
                for _ in range(distance):
                    position += 1
                    if position > 99:
                        position = 0
                    if position == 0:
                        count += 1
            elif direction == "R":
                for _ in range(distance):
                    position -= 1
                    if position < 0:
                        position = 99
                    if position == 0:
                        count += 1
        return count


day = Day1()
day.run(day.part_one, day.part_two)
