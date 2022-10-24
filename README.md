# Memory Game

[![Python_version](https://img.shields.io/badge/Python-v3.10.2-blueviolet?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3102/)
![License](https://custom-icon-badges.herokuapp.com/github/license/FranGarcia94/Memory-Game?logo=law)
![Size](https://badge-size.herokuapp.com/FranGarcia94/Memory-Game/main/memory_game.py)

<p align = "center">
<a href="https://github.com/FranGarcia94/Memory-Game"><img src="./images/hard_ingame.jpg"/></a>
</p>
<p align = "center">
<b>Number Memory Game made with tkinter in Python.</b>
</p>

# Game

![Tkinter](https://img.shields.io/badge/Tkinter-orange?style=flat)
![random](https://img.shields.io/badge/random-darkred?style=flat)

The board is divided into two parts, blue and green. In each part there are exactly the same numbers, the game consists of finding the pairs of each number in the shortest possible time.

![game_gif](./images/gif_1.gif)

## Start Window

![start_window](./images/init_window.jpg)

Here you can select the level of the game. As we will see later, the level will affect the size of the matrix.

## 1. Easy Mode ##
**4x4 matrix - 8 pairs of numbers (0-7)**

![easy_mode](./images/easy_mode.jpg)

## 2. Hard Mode ##
**8x8 matrix - 16 pairs of numbers (0-15)**

![hard_mode](./images/hard_mode.jpg)

## 3. Extreme Mode ##
**12x12 matrix - 36 pairs of numbers (0-35)**

![extreme_mode](./images/extreme_mode.jpg)

## Menu

Simple menu where we can choose a new level without restarting the game and also activate the flash mode.

| |  | |
| -- | -- | -- |
|![](./images/menu_easy.jpg) |![](./images/menu_easy_2.jpg) |![](./images/menu_extreme.jpg) |
|![](./images/menu_flash.jpg) |![](./images/menu_flash_on.jpg) |![](./images/menu_flash_on_2.jpg) |

### Flash mode

If activated, the two buttons will flash when a pair is found.

## WIN

When the game ends, a congratulation frame will appear and then the time it has lasted.

| |  | |
| -- | -- | -- |
|![](./images/winner_board.jpg) |![](./images/winner_congrat.jpg) |![](./images/winner_time.jpg) |

![win_gif](./images/gif_3.gif)
