from src.pattern_creator import PatternCreator
import numpy as np


class Cycler(PatternCreator):

    def __init__(self, dims: list[int]):
        super().__init__(dims)
        self.step = 0
        self.pos = np.zeros(self.dims)
        self.direction = 1

    def create_pattern(self) -> np.array:
        pattern = np.zeros(self.dims)
        pos = self.pos.copy()
        pos[0] = self.dims[0] - pos[0]
        pattern[pos] = 1
        sum_dims = sum(self.dims)
        cumsums = np.cumsum(self.dims)
        next_step = (self.step + 1) % sum_dims
        for index, cumsum in enumerate(cumsums):
            if cumsum > next_step:
                direction_index = index
                break
        self.pos[direction_index] += self.direction
        if self.step == sum_dims - 1:
            self.direction = -self.direction
        self.step = next_step
        return pattern
