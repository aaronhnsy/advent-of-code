import functools

import z3

from aoc import Day


class Machine:

    def __init__(self, line: str) -> None:
        lights, *buttons, voltages = line.split(" ")
        self.lights: list[int] = [0 if light == "." else 1 for light in lights[1:-1]]
        self.buttons: list[list[int]] = [[*map(int, button[1:-1].split(","))] for button in buttons]
        self.voltages: list[int] = [*map(int, voltages[1:-1].split(","))]

    def __repr__(self) -> str:
        return f"<Machine lights={self.lights}, buttons={self.buttons}, voltages={self.voltages} goal={self.goal}>"

    @functools.cached_property
    def goal(self) -> int:
        return sum(2 ** index for index, light in enumerate(self.lights) if light == 1)

    @functools.cached_property
    def button_scores(self) -> list[int]:
        return [sum(2 ** light for light in button) for button in self.buttons]


class Day10(Day[list[Machine]]):

    def parse(self) -> list[Machine]:
        return [*map(Machine, self.LINES)]

    def part_one(self):
        total_presses = 0
        for machine in self.input:
            min_presses = len(machine.buttons)
            for mask in range(2 ** len(machine.buttons)):
                current = 0
                presses = 0
                for index in range(len(machine.buttons)):
                    if ((mask >> index) % 2) != 1:
                        continue
                    current ^= machine.button_scores[index]
                    presses += 1
                if current == machine.goal:
                    min_presses = min(min_presses, presses)
            total_presses += min_presses
        return total_presses

    def part_two(self):
        total_presses = 0
        for machine in self.input:
            optimiser: z3.Optimize = z3.Optimize()
            # create a variable for each button
            button_variables: list[z3.ArithRef] = [
                z3.Int(f"button_{index}")
                for index in range(len(machine.buttons))
            ]
            # minimise for the amount of button presses
            optimiser.minimize(sum(button_variables))
            # constrain each button to not be pressed a negative amount of times
            for button_variable in button_variables:
                optimiser.add(button_variable >= 0)
            # constrain each voltage to be the sum of the presses of each button that affects it
            for voltage_index, voltage in enumerate(machine.voltages):
                optimiser.add(
                    voltage == sum(
                        button_variables[button_index]
                        for button_index, button in enumerate(machine.buttons)
                        if voltage_index in button
                    )
                )
            # check the optimiser
            assert optimiser.check()
            # model the optimiser and sum the button presses
            model = optimiser.model()
            total_presses += sum([model[x].as_long() for x in button_variables])  # pyright: ignore
        return total_presses


day = Day10()
day.run(day.part_one, day.part_two)
