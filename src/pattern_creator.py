import numpy as np


class PatternCreator:

    def __init__(self, dims: list[int], config: dict):
        self.dims = dims
        self.config = config

    def create_pattern(self) -> np.array:
        raise NotImplementedError()
