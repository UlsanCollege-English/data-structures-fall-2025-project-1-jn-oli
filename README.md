[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JWEh_q2R)
# Multi-Queue Round-Robin Café (Interactive CLI)

## How to run

Open your terminal and go to the `src` folder of the project:
   ```bash
   cd src
   2, Run the café simulation program using:

python cli.py


Once the program starts, type your commands one by one (they are case-sensitive).
Example:

CREATE A 3
ENQ A latte
ENQ A tea
RUN 2 3


To end the program:

Press Enter on a blank line, or

Press Ctrl + C

The program will print the message:

Break time!


## How to run tests locally
1. Make sure you are in the **root directory** of your project (where the `src/` and `tests/` folders are located).

2. Run the following command in your terminal:
   ```bash
   python -m pytest -q


## Complexity Notes
 Queue Design
- Each queue is implemented as a **circular buffer** inside the `QueueRR` class (see `scheduler.py`).
- It uses a fixed-size list `_buf` and head/size pointers (`_head`, `_size`) to allow constant-time operations.
- This avoids using Python’s `deque` and ensures O(1) enqueue/dequeue efficiency.

### Time Complexity
- **Enqueue:** O(1) — inserting at the back of the circular buffer.  
- **Dequeue:** O(1) — removing from the front of the buffer.  
- **Run:** O(#turns + total_minutes_worked) — each task is processed once per turn until completion.
