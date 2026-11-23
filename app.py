from collections import deque
import streamlit as st

st.set_page_config(page_title="Search & Maze Simulator", layout="wide")
st.title("Search Algorithm Visualizer & Maze Solver")
st.write("Step through **Linear Search** and **Binary Search**, race them side by side, or solve a grid maze with **BFS** and **DFS**.")


def is_sorted_ascending(values):
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


def parse_number_list(raw_text):
    parts = [piece.strip() for piece in raw_text.split(",") if piece.strip()]
    return [int(piece) for piece in parts]


def linear_search_steps(values, target):
    steps = []
    comparisons = 0
    for idx, val in enumerate(values):
        comparisons += 1
        matched = val == target
        steps.append({
            "algorithm": "Linear Search",
            "index": idx,
            "comparisons": comparisons,
            "low": None,
            "mid": None,
            "high": None,
            "found": matched,
            "done": matched,
            "message": (
                f"Comparison {comparisons}: index {idx} has {val} == {target}. Target found!"
                if matched
                else f"Comparison {comparisons}: index {idx} has {val} != {target}. Moving right."
            ),
        })
        if matched:
            return steps

    steps.append({
        "algorithm": "Linear Search",
        "index": None,
        "comparisons": comparisons,
        "low": None,
        "mid": None,
        "high": None,
        "found": False,
        "done": True,
        "message": f"Checked all {len(values)} items ({comparisons} comparisons). {target} was not found.",
    })
    return steps


def binary_search_steps(values, target):
    steps = []
    comparisons = 0
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2
        val = values[mid]
        comparisons += 1

        if val == target:
            steps.append({
                "algorithm": "Binary Search",
                "index": mid,
                "comparisons": comparisons,
                "low": low,
                "mid": mid,
                "high": high,
                "found": True,
                "done": True,
                "message": f"Comparison {comparisons} (low={low}, mid={mid}, high={high}): values[{mid}] is {val} == {target}. Found!",
            })
            return steps
        elif val < target:
            steps.append({
                "algorithm": "Binary Search",
                "index": mid,
                "comparisons": comparisons,
                "low": low,
                "mid": mid,
                "high": high,
                "found": False,
                "done": False,
                "message": f"Comparison {comparisons} (low={low}, mid={mid}, high={high}): {val} < {target}, eliminating left half (new low = {mid + 1}).",
            })
            low = mid + 1
        else:
            steps.append({
                "algorithm": "Binary Search",
                "index": mid,
                "comparisons": comparisons,
                "low": low,
                "mid": mid,
                "high": high,
                "found": False,
                "done": False,
                "message": f"Comparison {comparisons} (low={low}, mid={mid}, high={high}): {val} > {target}, eliminating right half (new high = {mid - 1}).",
            })
            high = mid - 1

    steps.append({
        "algorithm": "Binary Search",
        "index": None,
        "comparisons": comparisons,
        "low": low,
        "mid": None,
        "high": high,
        "found": False,
        "done": True,
        "message": f"Range empty (low={low} > high={high}) after {comparisons} comparisons. {target} not found.",
    })
    return steps


MAZES = {
    "Winding Path": [
        "S..#.....",
        ".#.#.###.",
        ".#...#...",
        ".###.#.#.",
        ".....#.#.",
        ".###...#.",
        "...#.##..",
        ".#......G",
    ],
    "Dead-End Trap": [
        "S.#......",
        "..#..###.",
        "..#....#.",
        "..####.#.",
        ".......#.",
        ".#####.#.",
        ".......#.",
        "######..G",
    ],
}


def reconstruct_path(parent, start, goal):
    if goal not in parent and goal != start:
        return []
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    path.reverse()
    return path


def maze_search_steps(grid, algo):
    rows = len(grid)
    cols = len(grid[0])
    start = None
    goal = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "G":
                goal = (r, c)

    frontier = deque([start]) if algo == "BFS (Shortest Path)" else [start]
    visited = {start}
    parent = {}
    steps = []

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while frontier:
        current = frontier.popleft() if algo == "BFS (Shortest Path)" else frontier.pop()
        r, c = current
        reached_goal = current == goal
        path = reconstruct_path(parent, start, goal) if reached_goal else []

        steps.append({
            "current": current,
            "visited": set(visited),
            "path": set(path),
            "path_len": len(path),
            "found": reached_goal,
            "message": (
                f"Reached Goal G at {current} in {len(visited)} visited cells! Shortest/found path length: {len(path)} steps."
                if reached_goal
                else f"Visiting cell {current} ({len(visited)} cells visited so far)."
            ),
        })

        if reached_goal:
            return steps

        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            nxt = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                neighbors.append(nxt)

        if algo == "BFS (Shortest Path)":
            frontier.extend(neighbors)
        else:
            # Push in reverse so first direction is popped first in LIFO stack
            for nxt in reversed(neighbors):
                frontier.append(nxt)

    steps.append({
        "current": None,
        "visited": set(visited),
        "path": set(),
        "path_len": 0,
        "found": False,
        "message": f"No path to Goal G exists ({len(visited)} cells explored).",
    })
    return steps


tab1, tab2 = st.tabs(["List Search & Race", "Maze Solver (BFS vs. DFS)"])

with tab1:
    presets = {
        "Sorted sample": "4, 9, 15, 19, 24, 31, 38, 45, 52",
        "Larger sorted list": "2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 104, 120",
        "Unsorted list": "38, 4, 52, 15, 9, 24, 19",
    }

    preset_choice = st.selectbox("Choose a preset list", list(presets.keys()))
    raw_input = st.text_input("Or edit comma-separated whole numbers", value=presets[preset_choice])

    try:
        values = parse_number_list(raw_input)
    except ValueError:
        st.error("Please enter only whole numbers separated by commas (for example: 4, 9, 15, 24).")
        st.stop()

    if len(values) == 0:
        st.warning("Enter at least one number to run a search.")
        st.stop()

    sorted_ok = is_sorted_ascending(values)
    st.caption(f"List status: **{'Sorted ascending' if sorted_ok else 'Not sorted'}** ({len(values)} items)")

    target = int(st.number_input("Target number to find", value=38, step=1))
    mode = st.radio("Mode", ["Step-by-Step Visualizer", "Linear vs. Binary Race"], horizontal=True)

    if mode == "Step-by-Step Visualizer":
        algorithm = st.selectbox("Choose an algorithm", ["Linear Search", "Binary Search"])

        if algorithm == "Binary Search" and not sorted_ok:
            st.warning(
                "Binary Search requires a **sorted** list because it discards half the list based on whether the middle item is smaller or larger than the target. "
                "On an unsorted list, it can skip over your target! Switch to **Linear Search** or pick a sorted preset."
            )

        steps = (
            linear_search_steps(values, target)
            if algorithm == "Linear Search"
            else binary_search_steps(values, target)
        )

        step_num = st.slider("Step", min_value=1, max_value=len(steps), value=1, key="search_step")
        current = steps[step_num - 1]

        st.info(f"**Step {step_num} of {len(steps)}:** {current['message']}")

        m1, m2, m3 = st.columns(3)
        m1.metric("Comparisons So Far", current["comparisons"])
        m2.metric("Steps Total", len(steps))
        m3.metric("Status", "Found" if current["found"] else ("Not Found" if current["done"] else "Searching"))

        cols = st.columns(len(values))
        for i, val in enumerate(values):
            with cols[i]:
                tags = []
                if algorithm == "Binary Search" and current["mid"] is not None:
                    if current["low"] is not None and i == current["low"]:
                        tags.append("L")
                    if i == current["mid"]:
                        tags.append("M")
                    if current["high"] is not None and i == current["high"]:
                        tags.append("H")
                tag_text = f" [{'/'.join(tags)}]" if tags else ""

                if current["found"] and current["index"] == i:
                    st.success(f"**{val}**\n\nidx {i}{tag_text}")
                elif current["index"] == i:
                    st.warning(f"**{val}**\n\nidx {i}{tag_text}")
                else:
                    st.button(f"{val}\nidx {i}{tag_text}", key=f"cell_{i}_{step_num}", disabled=True)

    else:
        if not sorted_ok:
            st.warning(
                "This list is **not sorted**, so Binary Search results may not be reliable—use a sorted list for a fair Binary Search comparison."
            )

        lin_steps = linear_search_steps(values, target)
        bin_steps = binary_search_steps(values, target)
        lin_final = lin_steps[-1]
        bin_final = bin_steps[-1]

        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Linear Search")
            st.metric("Comparisons Needed", lin_final["comparisons"])
            st.metric("Steps Recorded", len(lin_steps))
            st.write(f"**Result:** {'Found' if lin_final['found'] else 'Not found'}")
            st.caption(lin_final["message"])

        with c2:
            st.subheader("Binary Search")
            st.metric("Comparisons Needed", bin_final["comparisons"])
            st.metric("Steps Recorded", len(bin_steps))
            st.write(f"**Result:** {'Found' if bin_final['found'] else 'Not found'}")
            st.caption(bin_final["message"])

with tab2:
    st.subheader("Grid Maze Solver")
    st.caption("Legend: **S** = Start, **G** = Goal, **#** = Wall, **■** = Current cell, **★** = Final path")

    m_col1, m_col2 = st.columns(2)
    with m_col1:
        maze_name = st.selectbox("Choose a maze", list(MAZES.keys()))
    with m_col2:
        maze_algo = st.selectbox("Pathfinding algorithm", ["BFS (Shortest Path)", "DFS (Deep Exploration)"])

    grid = MAZES[maze_name]
    m_steps = maze_search_steps(grid, maze_algo)
    m_step_num = st.slider("Maze Step", min_value=1, max_value=len(m_steps), value=1, key="maze_step")
    m_curr = m_steps[m_step_num - 1]

    st.info(f"**Step {m_step_num} of {len(m_steps)}:** {m_curr['message']}")

    mm1, mm2, mm3 = st.columns(3)
    mm1.metric("Cells Visited", len(m_curr["visited"]))
    mm2.metric("Final Path Length", m_curr["path_len"] if m_curr["found"] else 0)
    mm3.metric("Goal Status", "Reached" if m_curr["found"] else "Exploring")

    for r_idx, row in enumerate(grid):
        row_cols = st.columns(len(row))
        for c_idx, cell in enumerate(row):
            coord = (r_idx, c_idx)
            with row_cols[c_idx]:
                if cell == "#":
                    st.button("🧱", key=f"m_{maze_name}_{maze_algo}_{m_step_num}_{r_idx}_{c_idx}", disabled=True)
                elif coord in m_curr["path"]:
                    st.success(f"★ {cell if cell in ('S', 'G') else '·'}")
                elif coord == m_curr["current"]:
                    st.warning(f"■ {cell if cell in ('S', 'G') else '·'}")
                elif coord in m_curr["visited"]:
                    st.button(f"· ({r_idx},{c_idx})", key=f"m_{maze_name}_{maze_algo}_{m_step_num}_{r_idx}_{c_idx}", disabled=True)
                else:
                    st.button(cell if cell in ("S", "G") else " ", key=f"m_{maze_name}_{maze_algo}_{m_step_num}_{r_idx}_{c_idx}", disabled=True)