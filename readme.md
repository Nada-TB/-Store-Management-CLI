
# Store Management CLI

A Python-based command-line interface (CLI) application for managing user purchases and inventory. This project simulates a small store workflow where users can check their purchase history, buy items, and track inventory. Designed with modularity, clean error handling, and Pythonic patterns.

---

## Features

* **User Management**

  * Check if a user exists
  * Handle new and existing users
  * Fetch user purchase history

* **Inventory Management**

  * Check item availability
  * Track item quantities
  * Update inventory on purchases

* **Purchasing System**

  * Select items and quantities
  * Update user purchase records
  * Option to continue shopping

* **Interactive CLI Experience**

  * Friendly prompts and messages
  * Input validation with custom exceptions
  * Typing simulation effects for improved UX

---

## Project Structure

```
store-management-cli/
│
├── main.py                     # Main CLI script, orchestrates flow
├── dispatcher.py               # Dispatches choices to handlers
├── handlers.py                 # Functions for handling user actions
├── ui.py                       # User interface utilities (messages, typing effects)
├── utils.py                    # Input sanitization and reusable helper functions
├── inventory.py                # Inventory data and checks
├── purchases.py                # User purchase tracking and functions
├── exceptions.py               # Custom exceptions for validation
├── inventory.json              # Inventory data storage
├── users_purchases.json        # User purchase data storage
└── README.md                   # Project documentation
```

---

## Getting Started

### Prerequisites

* Python 3.10+

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Nada-TB/Store-Management-CLI.git
```

2. Navigate into the project folder:

```bash
cd Store-Management-CLI
```

3. Run the CLI application:

```bash
python main.py
```

---

## Usage

1. Launch the program with `python main.py`.

2. Choose an option from the menu:

* **1**: Fetch user purchases
* **2**: Start a purchase
* **3**: Exit the store

3. Follow the interactive prompts for each workflow.

4. Continue shopping by typing `yes` when prompted, or `no` to finish.

---

## Input Handling Improvements

* **Custom Exception Handling**: The CLI now uses custom exceptions (`ChoiceInvalidError`, `EmptyNameError`, `IsNotAlphaError`, `EmptyItemError`, `ItemQuantityError`) to handle invalid inputs gracefully.
* **Reusable Helper `get_valid_input()`**: A generic function ensures inputs like item name and quantity are repeatedly requested until valid, reducing code repetition.
* **Boolean Conversion for Yes/No**: User confirmation inputs are directly converted to boolean (`continue_shopping = answer == "yes"`) for clean loop control.
* **Centralized Loop Control**: The main loop handles choice selection, user context, and purchase flow without scattering `sys.exit()` calls throughout the code.

---

## Notes

* Data is stored **in JSON files**, making it persistent between runs.
* Designed as a **learning project** demonstrating modular Python code, CLI interaction, and clean input handling.

---

## Future Improvements

* Extend `get_valid_input()` to handle multiple exception types with custom messages per exception.
* Implement unit tests for all core functions.
* Add more Pythonic patterns (comprehensions, context managers) where applicable.
* Consider database integration for scalable inventory and user data.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Author

**[Nada-TB](https://github.com/Nada-TB)** – First Python project showcasing modular CLI design, inventory management, and user interaction.

---
