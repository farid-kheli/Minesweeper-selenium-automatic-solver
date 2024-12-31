# 🎮 Minesweeper Automation Solver

This project provides a professional automation solver for the classic Minesweeper game using Selenium. The solver interacts with the Minesweeper game on a webpage, extracts the game grid, and employs a strategic approach to solve the puzzle.

---

## ✅ Prerequisites

Before starting, ensure the following requirements are met:

- **Python 3.x** 🐍: Programming language used for the project.
- **Selenium** 🌐: Library for browser automation.
- **ChromeDriver** 🖥️: WebDriver for Google Chrome.

---

## ⚙️ Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/minesweeper-solver.git
    cd minesweeper-solver
    ```

2. **Install Dependencies**
    Install the required Python libraries:
    ```bash
    pip install selenium
    ```

3. **Set Up ChromeDriver**
    - Download ChromeDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the downloaded `chromedriver` executable in the project directory.

---

## 🚀 Usage

1. **Configure the Script**
   - Open the `minesweeper.py` file.
   - Update the `executable_path` in the `Service` object to point to your `chromedriver` file.

2. **Run the Solver**
    Execute the script in your terminal:
    ```bash
    python minesweeper.py
    ```

3. **Observe the Automation**
   - The script will open a browser, navigate to the Minesweeper game webpage, and attempt to solve the puzzle using its automated strategy.

---

## 🛠️ How It Works

1. **Navigate to the Game**: Opens the Minesweeper game webpage in a browser.
2. **Extract the Game Grid**: Reads the current state of the Minesweeper grid.
3. **Apply the Solving Strategy**: Uses logical techniques to identify safe cells to open or flag as mines.
4. **Interact with the Game**: Simulates mouse clicks and flags cells based on solver decisions.

---

## 🧩 Core Functions

- **`GetID(first, second)`**: Returns the cell ID based on row and column coordinates.
- **`define(i, j)`**: Identifies the state of a cell (open, flagged, or closed).
- **`fill()`**: Populates the path list with cell coordinates.
- **`Situation()`**: Evaluates the game state (win, lose, or ongoing).
- **`GetJ(Worde)`**: Extracts the column index from a coordinate string.
- **`GetI(Worde)`**: Extracts the row index from a coordinate string.
- **`DeleteItem(i)`**: Removes an item from the path list if all surrounding cells are open or flagged.
- **`check(i, j, num)`**: Validates and clicks cells based on the number of surrounding mines.
- **`newTable(table)`**: Generates a new table of cell IDs.
- **`method()`**: Implements the primary logic to solve the Minesweeper game.

---

## 🤝 Contributing

We welcome contributions to enhance this project! If you find bugs, have feature suggestions, or would like to add improvements, feel free to:

1. **Open an Issue**: Describe the problem or suggestion.
2. **Submit a Pull Request**: Propose your changes with proper documentation and testing.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this project within the terms of the license.

---

Thank you for checking out this project! 🚀

