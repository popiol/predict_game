from src.pattern_creator import PatternCreator
import numpy as np


class Cycler(PatternCreator):

    def __init__(self, dims: list[int]):
        super().__init__(dims)
        self.step = 0

    def create_pattern() -> np.array:
        pattern = np.zeros()
