from src.config import Config
import numpy as np


class Game:

    def __init__(self, config: Config):
        self.config = config

    def pick_sub_pattern(self, pattern: np.array):
        return pattern[-1, :]

    def run(self):
        n_correct = 0
        max_correct = 0
        for turn_index in range(self.config.max_n_turns):
            print("Turn", turn_index)
            pattern = self.config.creator.create_pattern()
            sub_pattern = self.pick_sub_pattern(pattern)
            if turn_index > 0:
                if sub_pattern == guessed:
                    n_correct += 1
                    print("Correct guess", f"({n_correct} so far)")
                    if n_correct > max_correct:
                        max_correct = n_correct
                    if n_correct >= self.config.min_n_correct:
                        print(n_correct, "correct guesses reached!!!")
                        break
                else:
                    n_correct = 0
                    print("Incorrect guess")
            guessed = self.config.guesser.guess_next(sub_pattern)
        print(
            "Failure.",
            "Only",
            max_correct,
            "correct guesses in a row, expected",
            self.config.min_n_correct,
        )