# Search Algorithm Visualizer & Maze Solver

> **Demo Video (30–120 seconds):** https://drive.google.com/file/d/1ZdtJHhOK4iz96jOBqmjCmivv-SMzPy14/view?usp=sharing

## Project Description & Purpose

The **Search Algorithm Visualizer & Maze Solver** is an interactive Python and Streamlit web application designed to help learners understand searching and grid pathfinding algorithms through step-by-step visual feedback.

Rather than relying on static code or console printouts alone, this simulator records each step of an algorithm's execution and lets users move through every check using a slider, live metrics, and plain-English explanations. Building on classroom exploration of search algorithms and algorithm visualization, it adds custom list inputs, precondition checks, a side-by-side comparison mode, and a grid maze solver.

## Features

- **Step-by-Step Search Visualizer:** Step through **Linear Search** and **Binary Search** one check at a time using a slider, with live `L` (`low`), `M` (`mid`), and `H` (`high`) indicators for Binary Search and clear status highlights (`Found`, `Not Found`, or `Searching`).
- **Plain-English Step Explanations:** Every step explains which index or range is being checked, whether the target matches or eliminates half of the remaining search space, and how many comparisons have occurred so far.
- **Preset & Custom Lists + Input Validation:** Choose from built-in presets (*Sorted sample*, *Larger sorted list*, *Unsorted list*) or enter custom comma-separated whole numbers, with friendly error messages for invalid or empty inputs.
- **Binary Search Precondition Warning:** Alerts users when running Binary Search on an unsorted list and explains why halving the search space assumes sorted order.
- **Linear vs. Binary Race Mode:** Compares Linear Search and Binary Search side by side on the same list and target, showing total comparisons needed, steps recorded, and final search results.
- **Maze Solver (BFS vs. DFS):** Step through grid mazes (*Winding Path* and *Dead-End Trap*) using **Breadth-First Search (BFS)** or **Depth-First Search (DFS)**, displaying cells visited, final path length, explored cells, and the highlighted path to Goal `G`.

## Installation

1. Clone this repository and open the project folder:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/search-maze-simulator.git](https://github.com/YOUR_USERNAME/search-maze-simulator.git)
   cd search-maze-simulator
