import numpy as np


class PatternGuesser:

    def __init__(self, dims: list[int], config: dict):
        self.dims = dims
        self.config = config

    def guess_next(self, last_pattern: np.array, last_correct: bool) -> np.array:
        raise NotImplementedError()
