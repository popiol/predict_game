# predict_game

This repository implements a playground for ML methods by setting up a simple problem of guessing a pattern.

## Game rules

In the simplest version, the game is using a squared board of 0/1 values.

```
0 1 0 0
0 1 0 0
0 1 0 0
0 1 1 1
```

In general, the board might be higher dimensional and have a different length in each dimension.

There are two players, one of them fills the board with 0/1 values to form a pattern and changes the pattern in each turn.
The other player can only see the last row of the board, 
and tries to guess what the values are going to be in the last row in the next turn.

It is important to note that the first player has to follow logical rules to change the pattern in each turn,
meaning that the patterns cannot be random.

The game ends when the second player correctly guesses the pattern required number of times in a row, 
or when the maximum number of turns is reached.

From the implementation perspective, the first player is hard-coded and the second player is the ML model.

## Example

Let's say the patterns simulate digit 1 traveling around the board. The first 4 patterns will look like this

```
0 0 0 0  0 0 0 0  0 0 0 0  0 0 0 0
0 0 0 0  0 0 0 0  0 0 0 0  0 0 0 0
0 0 0 0  0 0 0 0  0 0 0 0  0 0 0 0
1 0 0 0  0 1 0 0  0 0 1 0  0 0 0 1
```

The second player will only see the last row

```
1 0 0 0  0 1 0 0  0 0 1 0  0 0 0 1
```

Then there will only be zeros in the last row for the next 8 turns, and then the cycle will repeat.

## Running a game

python -m src.game --config configs/cycler.yml
