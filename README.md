
# ☕ Python OOP Coffee Machine App

This repository contains coffee machine simulation written in Python — designed with **Object-Oriented Programming (OOP)** principles.
It provides a more scalable and organized structure compared to the basic version.

Great for learning classes, objects, and modular code architecture! ✅

---

## 🚀 Features

- Object-Oriented structure using multiple classes:
  - `CoffeeMaker` — Manages ingredients and brewing
  - `MoneyMachine` — Handles coin input & payments
  - `Menu` & `MenuItem` — Holds drink data and pricing
- Clean and maintainable code architecture
- CLI-based user interaction
- Realistic resource checking and money handling
- Refunds when payment is insufficient
- Resource reports available anytime

---

## 🛠️ Requirements

- **Python 3.x**
- No external dependencies

---

## 📦 Installation & Usage

```bash
# Clone the project
git clone https://github.com/qazipoor/Python_OOP_Coffee_Machine.git
````

```bash
# Move into folder
cd Python_OOP_Coffe_Machine
```

```bash
# Run the program
python main.py
```

---

## ▶️ How to Play

- Order a drink by typing: `espresso`, `latte`, or `cappuccino`
- Insert coins when asked (quarters, dimes, nickels, pennies)
- Machine processes payment & delivers coffee if enough money
- Type `report` for current resource
- Type `profit` for earnings info
- Type `off` to power down the machine

---

## 📂 Project Structure

```
oop-coffee-machine/
│
├── main.py             # Execution script & user I/O
├── coffee_maker.py     # Handles resources (CoffeeMaker class)
├── money_machine.py    # Handles transactions (MoneyMachine class)
├── menu.py             # Menu & MenuItem classes
└── README.md           # This documentation
```

---

## 🧠 OOP Concepts Applied

| Concept | Demonstrated in |
|--------|-----------------|
| Classes & Objects | Resource & payments using class instances |
| Abstraction | Methods like make_coffee(), is_resource_sufficient() |
| Encapsulation | Resource and money hidden inside classes |
| Composition | MenuItem objects used by Menu |
| Separation of Concerns | Each class has a single responsibility |

---

## 🌟 Future Improvements

- Add more drink options
- GUI version (Tkinter / PyQt)
- Audio and animations 😄
- Persistence: Save and reload money/resources from file
- Automated tests

---

## 🤝 Contributing

Contributions are welcome — feel free to submit ideas or improvements!

---

## 📝 License

This project is open-source under the **MIT License**.

---

Enjoy your virtual caffeine! ☕💻
