from src.config import Config


class Game:

    def __init__(self, config: Config):
        self.config = config

    def run(self):
        n_correct = 0
        max_correct = 0
        for turn_index in range(self.config.max_n_turns):
            print("Turn", turn_index)
            pattern = self.config.creator.create_pattern()
            if turn_index > 0:
                if pattern == guessed:
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
            guessed = self.config.guesser.guess_next(pattern)
        print("Failure.", "Only", max_correct, "correct guesses in a row, expected", self.config.min_n_correct)
