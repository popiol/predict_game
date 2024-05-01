import numpy as np

from src.pattern_guesser import PatternGuesser


class BasicModel(PatternGuesser):

    def __init__(self, dims: list[int]):
        super().__init__(dims)
        self.step = 0

    def guess_next(last_pattern: np.array) -> np.array:
        pass
