from aoc import Day


class Day5(Day[None]):

    def __init__(self) -> None:
        self.fresh_ingredients: list[tuple[int, int]] = []
        self.available_ingredients: list[int] = []
        super().__init__()

    @staticmethod
    def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        if not ranges:
            return []
        ranges.sort(key=lambda x: x[0])
        merged = [ranges[0]]
        for current in ranges[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
        return merged

    def parse(self) -> None:
        data: list[str] = self.TEXT.split("\n\n")
        self.fresh_ingredients = [
            tuple[int, int](map(int, x.split("-")))
            for x in data[0].split("\n")
        ]
        self.available_ingredients = list(map(int, data[1].split("\n")))

    def part_one(self) -> int:
        return len(
            [*filter(
                lambda ingredient:
                    any(low <= ingredient <= high for low, high in self.fresh_ingredients),
                self.available_ingredients,
            )]
        )

    def part_two(self) -> int:
        return sum(
            max(r) - min(r) + 1
            for r in self.merge_ranges(self.fresh_ingredients)
        )


day = Day5()
day.run(day.part_one, day.part_two)
