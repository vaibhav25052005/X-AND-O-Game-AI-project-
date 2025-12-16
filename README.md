Project Description: X and O Game (Tic-Tac-Toe) with AI

The X and O (Tic-Tac-Toe) Game with Artificial Intelligence is a Python-based project that demonstrates how intelligent decision-making can be applied to a classic turn-based game. The project allows a human player to play against an AI opponent in a simple and interactive environment, making it both educational and engaging.

The game is built around a 3×3 grid where the human player uses X and the AI uses O. The program manages the game flow by alternating turns between the player and the AI. User input is validated to ensure that moves are placed only in empty cells and within valid positions. After each move, the system checks for winning conditions by evaluating rows, columns, and diagonals. If all positions are filled without a winner, the game correctly identifies the match as a draw.

The AI component is designed to play intelligently rather than randomly. It evaluates the current state of the board and selects the best possible move using strategic logic or algorithms such as Minimax. By predicting possible future moves, the AI attempts to maximize its chances of winning while minimizing the player’s opportunities, making the game challenging and realistic.

This project highlights essential Artificial Intelligence concepts such as game state evaluation, adversarial decision-making, and optimal move selection. It also reinforces core Python programming skills, including the use of functions, loops, conditional statements, lists, and logical operators. The modular structure of the code improves readability and allows easy expansion.

The X and O Game with AI project is ideal for beginners and students exploring AI through practical implementation. It can be further enhanced by adding features like a graphical user interface, multiple difficulty levels, or online multiplayer support, making it a strong foundation for advanced game development and AI learning.
Below is a **clear step-by-step explanation of how your X and O (Tic-Tac-Toe) AI code works**, from top to bottom, in **simple language**.
(Explained using your uploaded file) 

---


This program creates an **unbeatable Tic-Tac-Toe game** using the **Minimax algorithm with Alpha-Beta pruning**, where a human plays against an AI.

---

## **2. Imports**

```python
import math
import random
from typing import List, Optional, Tuple
```

* `math` → used for infinity values (`±inf`)
* `random` → fallback random move
* `typing` → improves code clarity and structure

---

## **3. Winning Positions**

```python
WIN_COMBINATIONS = [(0,1,2), (3,4,5), ...]
```

These are all possible **winning line combinations** (rows, columns, diagonals).

---

## **4. Board Class**

Handles everything related to the game board.

### **Board Creation**

```python
self.cells = [' '] * 9
```

Creates a 3×3 board (9 empty cells).

### **Make Move**

```python
make_move(idx, player)
```

Places `X` or `O` only if the cell is empty.

### **Available Moves**

```python
available_moves()
```

Returns all empty positions.

### **Winner Check**

```python
check_winner()
```

Checks all win combinations and returns the winner.

### **Clone Board**

```python
clone()
```

Creates a copy of the board for AI simulations.

---

## **5. Scoring System**

```python
score_for_winner()
```

* AI wins → `+1`
* Human wins → `-1`
* Draw → `0`

This helps the AI decide the best move.

---

## **6. Minimax Algorithm (AI Brain)**

```python
minimax(board, depth, maximizing, alpha, beta)
```

### **How it works**

* AI tries to **maximize** the score
* Human tries to **minimize** the score
* Simulates **all possible future moves**
* Chooses the best possible outcome

### **Alpha-Beta Pruning**

```python
if beta <= alpha:
    break
```

Stops checking useless paths → **faster AI**

---

## **7. Best Move Selection**

```python
best_move_for_ai()
```

* If board is empty → take center
* Otherwise → run Minimax
* If no move found → choose random

---

## **8. User Input**

```python
input_move_from_user()
```

* Accepts values `1–9`
* Prevents invalid or occupied moves
* Allows quitting the game

---

## **9. Symbol Selection**

```python
choose_symbol()
```

User chooses **X or O**

* X always plays first

---

## **10. Main Game Loop**

```python
while True:
```

* Prints board
* Checks win or draw
* Human and AI take turns
* Switches players each move

---

## **11. Game End**

Displays final board and result:

* AI win
* Human win
* Draw

---

## **Summary**

✔ Uses **Minimax + Alpha-Beta pruning**
✔ AI always plays optimally
✔ Demonstrates **game theory & AI logic**
✔ Strong project for **AI / ML / Python portfolios**
