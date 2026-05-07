# 🌊 Coral-Wave — Beach Shop Simulation

**Coral-Wave** is a modular Python-based console application that simulates a beach shop experience, allowing users to browse products, manage a cart, and generate structured purchase receipts.

Designed with clean architecture and user-centric logic, the project demonstrates strong fundamentals in Python application design, input validation, and modular development.

---

## 🚀 Features

- 🏖️ Multi-section shopping system:
  - Beach Products
  - Skin Care
  - Clothing
- 🔄 Continuous shopping loop with exit control  
- 🧾 Per-section and global receipt generation  
- 🔢 Number-based menu navigation (no fragile string input)  
- 🛡️ Robust input validation and error handling  
- 👤 Customer interaction flow (name, age, decisions)

---

## 🧠 Architecture & Design

The project evolved from a monolithic script into a **clean, modular structure**, improving scalability and maintainability:

```bash
main.py        # Entry point
app.py         # Core application logic
products.py    # Product definitions
models.py      # Data structures (cart, items, etc.)
```

---

## 🛠️ Technologies

- Python 3  
- Object-Oriented Programming (OOP)  
- Modular Design Principles
