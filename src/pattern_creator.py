import numpy as np


class PatternCreator:

    def __init__(self, dims: list[int]):
        self.dims = dims

    def create_pattern(self) -> np.array:
        raise NotImplementedError()
