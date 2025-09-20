# Store Management CLI

A command-line interface (CLI) application for managing user purchases and inventory. This project simulates a small store workflow where users can check their purchase history, buy items, and track inventory. Built in Python as a learning project with modular design.

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
  * Typing simulation effects for improved UX

---

## Project Structure

```
store-management-cli/
│
├── script.py                  # Main CLI script
├── ui.py                      # User interface utilities (messages, typing effects)
├── utils.py                   # Input sanitization and helper functions
├── inventory.py               # Inventory data and checks
├── purchases.py               # User purchase tracking and functions
└── README.md                  # Project documentation
```

---

## Getting Started

### Prerequisites

* Python 3.10+ (required for `match/case` statements)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/store-management-cli.git
   ```
2. Navigate into the project folder:

   ```bash
   cd store-management-cli
   ```
3. Run the CLI application:

   ```bash
   python script.py
   ```

---

## Usage

1. Launch the program with `python script.py`.

2. Choose an option from the menu:

   * **1**: Fetch user purchases
   * **2**: Start a purchase
   * **3**: Exit the store

3. Follow the interactive prompts for each workflow.

---

## Notes

* Data is stored **in memory**, so purchases and inventory are reset on each run.
* Designed as a **learning project** to demonstrate modular Python coding, CLI interaction, and basic problem-solving.

---

## Future Improvements

* Persist data to JSON or a database
* Add error handling for invalid numeric input
* Refactor for more Pythonic patterns (comprehensions, context managers)
* Add unit tests for core functions

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Author

**\[Nada]** – First Python project showcasing modular CLI design, inventory management, and user interaction.

---
