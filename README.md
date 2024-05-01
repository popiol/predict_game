# predict_game

This repository implements a playground for ML methods by setting up a simple problem of guessing a pattern.

# Game rules

In the simples version, the game is using a squared board of 0/1 values.

``
0 1 0 0
0 1 0 0
0 1 0 0
0 1 1 1
``

In general, the board might be higher dimensional and have a different length in each dimension.

There are two players, one of them fills the board with 0/1 values to form a pattern and changes the pattern in each turn.
The other player can only see the last row of the board, 
and tries to guess what the values are going to be in the last row in the next turn.

The important thing to note is that the first player has to follow some logical rules to change the pattern in each turn,
meaning that the patterns cannot be random.
