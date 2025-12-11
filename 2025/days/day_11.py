import functools

from aoc import Day


class Day11(Day[dict[str, list[str]]]):

    def parse(self) -> dict[str, list[str]]:
        return {
            machine: outputs.lstrip().split(" ")
            for machine, outputs in map(lambda line: line.split(":"), self.LINES)
        }

    def part_one(self) -> int:
        @functools.cache
        def check(machine: str, paths: int = 0) -> int:
            return paths + (
                1 if ("out" in self.input[machine])
                else sum(map(
                    lambda output: check(output, paths),
                    self.input[machine]
                ))
            )

        return check("you")

    def part_two(self) -> int:
        @functools.cache
        def check(machine: str, paths: int = 0, dac: bool = False, fft: bool = False) -> int:
            return paths + (
                (1 if (dac and fft) else 0) if ("out" in self.input[machine])
                else sum(map(
                    lambda output: check(output, paths, dac or machine == "dac", fft or machine == "fft"),
                    self.input[machine],
                ))
            )

        return check("svr")


day = Day11()
day.run(day.part_one, day.part_two)
