from src.pattern_creator import PatternCreator
import numpy as np


class Cycler(PatternCreator):

    def __init__(self, dims: list[int], config: dict):
        super().__init__(dims, config)
        self.step = self.dims[0] - 1
        self.pos = np.zeros(len(self.dims), dtype=int)
        self.pos[0] = self.dims[0] - 1
        self.direction = 1

    def create_pattern(self) -> np.array:
        pattern = np.zeros(self.dims, dtype=int)
        pattern[tuple(self.pos)] = 1
        sum_dims = sum(self.dims)
        cumsums = np.cumsum([x - 1 for x in self.dims])
        next_step = (self.step + 1) % (sum_dims - len(self.dims))
        for index, cumsum in enumerate(cumsums):
            if cumsum > self.step:
                direction_index = index
                break
        self.pos[direction_index] += self.direction
        if self.step == sum_dims - len(self.dims) - 1:
            self.direction = -self.direction
        self.step = next_step
        return pattern
