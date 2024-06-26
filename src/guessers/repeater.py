import numpy as np

from src.pattern_guesser import PatternGuesser


class Repeater(PatternGuesser):

    def __init__(self, dims: list[int], config: dict):
        super().__init__(dims, config)
        self.step = 0

    def guess_next(self, last_pattern: np.array) -> np.array:
        return last_pattern
