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
   git clone [https://github.com/jadedodds/search-maze-simulator.git](https://github.com/jadedodds/search-maze-simulator.git)
   cd search-maze-simulator

2. Install the required dependency (`streamlit`):
   ```bash
   python3 -m pip install -r requirements.txt

## How to Run

From inside the `search-maze-simulator` folder, start the Streamlit server:

```bash
python3 -m streamlit run app.py
Your default web browser will open the app (typically at http://localhost:8501 or http://localhost:8502). To stop the app later, click in your terminal and press Ctrl + C.

How to Use It
List Search & Race tab:

Pick a preset list or type your own comma-separated numbers, then choose the Target number to find.

Keep Mode on Step-by-Step Visualizer, pick Linear Search or Binary Search, and drag the Step slider forward and backward to inspect each comparison.

Switch Mode to Linear vs. Binary Race to compare how many comparisons and steps each algorithm takes on the same input.

Maze Solver (BFS vs. DFS) tab:

Select a maze (Winding Path or Dead-End Trap) and choose BFS (Shortest Path) or DFS (Deep Exploration).

Drag the Maze Step slider to watch cells get explored step by step and see the final path once Goal G is reached.

Lessons Learned
Recording step history makes visualizers flexible: Storing each step as a structured dictionary (with indices, pointers, comparison counts, and a plain-English message) made scrubbing forward and backward through a search or maze much cleaner than printing inside a loop.

Preconditions matter in interactive tools: Testing Binary Search on unsorted data highlighted why clear warnings and input validation are essential so users don't get misleading results.

Small setup and workflow details matter: Getting a clean local environment running—trusting the workspace folder, saving changes (Cmd + S) before rerunning, and launching with python3 -m streamlit run app.py instead of bare python3 app.py—made iterating on features much smoother.

Opportunities
Auto-play and speed control: Add a Play/Pause button and speed slider so users can watch step-by-step animations advance automatically in addition to dragging the slider manually.

Interactive maze builder and A* search: Let users toggle walls, start (S), and goal (G) cells directly on the grid, and add A* alongside BFS and DFS.

Additional algorithms and charts: Add interpolation search, recursive binary search, or a comparison chart showing how search counts scale as list size grows.

Wins
Built a complete, multi-tab interactive learning simulator in Python and Streamlit combining step-by-step search visualization, a Linear vs. Binary Race mode, and a BFS/DFS grid maze solver.

Designed plain-English explanations and live counters so learners can see why each step happens, not just which item or cell changes.

Worked through the setup and build stages step by step until both tabs ran reliably in the browser with clear feedback and edge-case checks.
