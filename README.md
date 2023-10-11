# TicTacToeMinMax

Simple console application implementing TicTacToe game with MinMax algorithm.

## How to run

```
git clone https://github.com/hubertpytkiewicz/TicTacToeMinMax.git
cd TicTacToeMinMax
python3 main.py [optional_argument]
```

## Options for running script

* ```rva``` - Random player vs AI player (default)
* ```hva``` - Human player vs AI player
* ```hvr``` - Human player vs Random player
* ```aitest``` - Allows to run ```rva``` for specified number of times and see the statistics of _w/d/l_

## How to play
```
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
```
If you want to place your mark in one of the 9 spaces, simply input the number of the space that is not taken yet.

## Test example

```
| X | O | X |

| X | X | O |

| O | X | O |

Tie...
Random player won 0 times.
AI player won 791 times.
There were 209 ties.
It took 231.02245545387268 seconds.
```