# 8-Puzzle Solver: Heuristic Search Experiments

This repository contains Python implementations of various local search algorithms used to solve the classic **8-Puzzle problem**. The project explores the trade-offs between greedy approaches and probabilistic metaheuristics to overcome the challenge of local optima.

---

## 🚀 Implemented Algorithms

The solver includes three primary search strategies:

* **Hill Climbing:** A greedy local search that always moves to the neighbor with the best heuristic score. It is fast but prone to getting stuck in local optima.
* **Simulated Annealing:** A probabilistic technique inspired by metallurgy. It allows for "downhill" moves (moving to a worse state) based on a probability that decreases over time (temperature cooling), enabling the solver to escape local traps.
* **Random Restart Simulated Annealing:** A meta-strategy that runs the Simulated Annealing algorithm multiple times and selects the most successful or shortest path found across all iterations.



---

## 🧠 Heuristics

The current implementation uses the **Misplaced Tiles** heuristic:
- **Score:** Count of tiles that are not in their correct goal position.
- **Goal:** Minimize the score to **0**.

---

## 🛠️ Project Structure

* `hillClimbing(init, goal)`: Executes a standard greedy search.
* `simulatedAnnealing(init, goal, temp)`: A single run of SA with visual board output.
* `randRestartAnnealing(init, goal, temp, n)`: Runs the solver $n$ times and identifies the best path.
* `getNeighbours(state)`: Generates valid moves (Up, Down, Left, Right) by identifying the "zero" (empty) tile and creating state copies.

---

## 💻 How to Run

1. **Prerequisites:** Python 3.x installed.
2. **Setup:** Save the script as `solver.py`.
3. **Execution:**
   ```bash
   python solver.py

## Customization

Modify the init2 or goal variables in the code to test different configurations.

## 📈 Optimization Details

To ensure efficient execution and accurate results:
* Fast State Copying: Uses list comprehension [row[:] for row in state] to prevent unintentional reference mutations.
* Geometric Cooling: The temperature in Simulated Annealing decays by a factor of $0.99$ every iteration to transition from exploration to exploitation.
* Path Tracking: Returns the full sequence of moves and board states for the best solution found.

## 📝 Future Roadmap
* Manhattan Distance: Implement a more granular heuristic for faster convergence.
* *A Search:** Implement an optimal search using a Priority Queue.
* React Visualizer: Build a web interface to visualize the search process.
