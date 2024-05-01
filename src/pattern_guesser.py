import numpy as np


class PatternGuesser:

    def __init__(self, dims: list[int]):
        self.dims = dims

    def guess_next(last_pattern: np.array) -> np.array:
        raise NotImplementedError()
