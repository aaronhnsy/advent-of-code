import pathlib
import time
import timeit
from collections.abc import Callable

__all__ = ["Day"]

type PartReturn = int | str
type Part = Callable[[], PartReturn]


class Day[T]:

    def __init__(self) -> None:
        self.FILE: str = f"../inputs/{self.__class__.__name__.lower()}.txt"
        self.LINES: list[str] = pathlib.Path(self.FILE).read_text().splitlines()
        self.INPUT: T = self.parse()

    def parse(self) -> T:
        raise NotImplementedError

    def part_one(self) -> PartReturn:
        raise NotImplementedError

    def part_two(self) -> PartReturn:
        raise NotImplementedError

    @staticmethod
    def run(*parts: Part) -> None:
        for i, part in enumerate(parts, start=1):
            start = time.perf_counter()
            print(f"Part {i}: {part()} (took {round(time.perf_counter() - start, 5)}s)")

    @staticmethod
    def time(*parts: Part, count: int = 500) -> None:
        for i, part in enumerate(parts, start=1):
            average = (timeit.timeit(part, number=count) / count) * 1000000
            print(f"Part {i}: {part()} ({average:.3f}µs @ {count:,} runs)")
