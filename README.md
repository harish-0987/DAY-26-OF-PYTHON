# Day 26: Object-Oriented Programming (OOP) - Encapsulation in Python 🔒💊🐍

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-26-OF-PYTHON](https://github.com/harish-0987/DAY-26-OF-PYTHON)

Welcome to **Day 26 of Python**! Today's session is dedicated to **Encapsulation in Python**—one of the core pillars of Object-Oriented Programming (OOP)—explored at a clear, practical, beginner-friendly foundational level.

> [!NOTE]
> **Scope for Today**: We demystify the concept of **Encapsulation** (bundling data and methods while restricting direct access), the real-world analogies (medical capsule, bank vault, ATM), access modifiers in Python (Public, Protected `_`, and Private `__`), Name Mangling, traditional getter/setter validation, Pythonic property decorators (`@property`, `@setter`, `@deleter`), private internal helper methods, and a complete real-world banking wallet case study.

---

## 📌 Table of Contents

1. [What is Encapsulation? (Basic Level)](#-what-is-encapsulation-basic-level)
2. [Why Use Encapsulation?](#-why-use-encapsulation)
3. [Access Modifiers in Python](#-access-modifiers-in-python)
   - [1. Public Members](#1-public-members)
   - [2. Protected Members (`_single_underscore`)](#2-protected-members-_single_underscore)
   - [3. Private Members (`__double_underscore`) & Name Mangling](#3-private-members-__double_underscore--name-mangling)
4. [Controlling Access: Traditional Getters & Setters](#-controlling-access-traditional-getters--setters)
5. [Pythonic Encapsulation with `@property` Decorator](#-pythonic-encapsulation-with-property-decorator)
6. [Private Helper Methods (Hiding Internal Logic)](#-private-helper-methods-hiding-internal-logic)
7. [Real-World Project: Secure Bank Account & Smart Wallet](#-real-world-project-secure-bank-account--smart-wallet)
8. [Quick Summary Comparison Matrix](#-quick-summary-comparison-matrix)
9. [Code Implementation & Running the Code](#-code-implementation--running-the-code)

---

## 💡 What is Encapsulation? (Basic Level)

**Encapsulation** is the mechanism of wrapping data (attributes/variables) and the code that operates on that data (methods/functions) together into a single unit (a class), while simultaneously restricting direct unauthorized access to internal state.

```
       ┌────────────────────────────────────────────────────────┐
       │                       CLASS                            │
       │                                                        │
       │   ┌────────────────────────────────────────────────┐   │
       │   │  PRIVATE DATA (Protected Internal State)       │   │
       │   │  • __balance                                   │   │
       │   │  • __pin                                       │   │
       │   │  • __transaction_history                       │   │
       │   └───────────────────────▲────────────────────────┘   │
       │                           │ Controlled Access          │
       │   ┌───────────────────────▼────────────────────────┐   │
       │   │  PUBLIC INTERFACE (Methods & Properties)       │   │
       │   │  • deposit(amount)                             │   │
       │   │  • withdraw(amount, pin)                       │   │
       │   │  • check_balance(pin)                          │   │
       │   └───────────────────────▲────────────────────────┘   │
       └───────────────────────────┼────────────────────────────┘
                                   │
                           EXTERNAL CALLER
                        (Cannot tamper with data)
```

### 💊 Real-World Analogies

1. **Medical Capsule**:
   - The capsule shell packages multiple medicinal powders together. You consume the pill safely as a unit without tampering with the individual chemical particles inside.
2. **ATM / Bank Vault**:
   - You cannot walk directly into a bank vault and pick up cash. Instead, you interact with authorized public entry points: insert card, enter PIN, choose deposit or withdrawal. The internal vault stays secure.
3. **Automobile Dashboard**:
   - You drive a car using the steering wheel, accelerator, and brake pedals. You don't directly adjust fuel injection lines or combustion chambers while driving.

---

## 🚀 Why Use Encapsulation?

1. **Data Hiding & Security**: Keeps internal sensitive data safe from external corruption or accidental modification.
2. **Data Integrity & Validation**: Setters validate inputs before accepting changes (e.g., negative balance rejection, age > 0).
3. **Flexibility & Read-Only Attributes**: Easily create read-only properties by providing a getter without a setter.
4. **Maintainability & Modularity**: You can refactor or optimize internal algorithms without breaking any client code that relies on your public interface.

---

## 🔒 Access Modifiers in Python

Unlike languages like Java or C++ that feature strict keywords (`public`, `protected`, `private`), Python relies on **naming conventions with underscores**:

| Access Level | Naming Convention | Example | Accessibility |
| :--- | :--- | :--- | :--- |
| **Public** | Standard name | `self.name` | Accessible anywhere (inside, subclasses, outside) |
| **Protected** | Single leading underscore | `self._founded_year` | Convention: Accessible inside class & subclasses |
| **Private** | Double leading underscore | `self.__secret_code` | Enforced via Name Mangling: Hidden from outside |

---

### 1. Public Members
Public members are accessible from anywhere without restriction:

```python
class Student:
    def __init__(self, name: str, roll_no: int):
        self.name = name          # Public
        self.roll_no = roll_no    # Public

s = Student("Harish", 101)
print(s.name)      # Read directly -> "Harish"
s.roll_no = 102    # Modify directly
```

---

### 2. Protected Members (`_single_underscore`)
In Python, prefixing an attribute or method with a single underscore `_` tells other programmers:
> *"This is an internal/protected implementation detail. Please do not modify it directly outside this class or its subclasses."*

```python
class Company:
    def __init__(self, name: str, year: int):
        self.name = name
        self._founded_year = year   # Protected attribute

class Branch(Company):
    def show_info(self):
        # Accessible in subclass
        print(f"{self.name} was founded in {self._founded_year}")
```

> [!IMPORTANT]
> Python does not physically prohibit external code from reading `obj._founded_year`. It relies on developer discipline and PEP 8 convention.

---

### 3. Private Members (`__double_underscore`) & Name Mangling
When you prefix an attribute or method with **two leading underscores** `__`:
- Python restricts direct outside access and raises an `AttributeError`.
- It activates **Name Mangling**: Python internally renames `__attribute` to `_ClassName__attribute`.

```python
class SafeBox:
    def __init__(self, secret: str):
        self.__secret_code = secret  # Private attribute

box = SafeBox("CLASSIFIED-9988")

# Attempting direct access:
# print(box.__secret_code) 
# -> AttributeError: 'SafeBox' object has no attribute '__secret_code'

# Name Mangling in action (behind the scenes):
print(getattr(box, "_SafeBox__secret_code")) # "CLASSIFIED-9988"
```

---

## 🛠️ Controlling Access: Traditional Getters & Setters

Getters (*Accessors*) and Setters (*Mutators*) allow controlled inspection and modification of private attributes with validation rules:

```python
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = 0.0
        self.set_salary(salary)

    # Getter
    def get_salary(self) -> float:
        return self.__salary

    # Setter with validation
    def set_salary(self, amount: float) -> None:
        if amount <= 0:
            print("Error: Salary must be positive!")
            return
        self.__salary = float(amount)
```

---

## 🐍 Pythonic Encapsulation with `@property` Decorator

Python provides `@property` so you can access methods using attribute syntax while still enforcing validation logic:

```python
class TemperatureSensor:
    def __init__(self, celsius: float):
        self._celsius = 0.0
        self.celsius = celsius  # Triggers setter validation

    # Getter
    @property
    def celsius(self) -> float:
        return self._celsius

    # Setter with validation
    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15 C)!")
        self._celsius = float(value)

    # Read-Only Property (No setter defined)
    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32
```

---

## 🔒 Private Helper Methods (Hiding Internal Logic)

Encapsulation extends to internal implementation methods. Public APIs coordinate multiple private steps:

```python
class EmailService:
    def __init__(self, sender: str):
        self.sender = sender

    # Private helper method
    def __authenticate_smtp(self) -> bool:
        return True

    # Public interface
    def send_email(self, recipient: str, message: str) -> bool:
        if not self.__authenticate_smtp():
            return False
        print(f"Email sent to {recipient}!")
        return True
```

---

## 🏦 Real-World Project: Secure Bank Account & Smart Wallet

A full-scale implementation integrating all encapsulation principles:
- **Public**: `holder_name`, `account_type`
- **Read-Only Properties**: `account_number` (masked), `account_tier`
- **Protected**: `_tier`
- **Private**: `__balance`, `__pin`, `__transaction_history`
- **Controlled Methods**: `deposit()`, `withdraw()`, `check_balance()`, `change_pin()`, `print_mini_statement()`

```
-----------------------------------------------------------------
 MINI-STATEMENT: Harish (*******1098)
 Tier: Gold | Available Balance: $6,300.00
-----------------------------------------------------------------
Timestamp            | Type            | Amount     | Balance
-----------------------------------------------------------------
2026-10-03 21:13:14  | OPENING_DEPOSIT | $6000.00   | $6,000.00
2026-10-03 21:13:14  | DEPOSIT         | $1500.00   | $7,500.00
2026-10-03 21:13:14  | WITHDRAWAL      | $1200.00   | $6,300.00
-----------------------------------------------------------------
```

---

## 📊 Quick Summary Comparison Matrix

| Feature | Public | Protected (`_`) | Private (`__`) | Property (`@property`) |
| :--- | :--- | :--- | :--- | :--- |
| **Syntax** | `self.val` | `self._val` | `self.__val` | `@property` / `@val.setter` |
| **Accessible Inside Class?** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Accessible in Subclasses?**| ✅ Yes | ✅ Yes | ❌ No (Name mangled) | ✅ Yes |
| **Accessible Outside?** | ✅ Yes | ⚠️ By convention only | ❌ No (AttributeError) | ✅ Controlled via methods |
| **Validation Enabled?** | ❌ No | ❌ No | ❌ No | ✅ Yes (in setter) |
| **Primary Use Case** | General API | Internal class state | Sensitive & hidden state | Pythonic controlled access |

---

## 💻 Code Implementation & Running the Code

### Clone or Pull the Repository
```bash
git clone https://github.com/harish-0987/DAY-26-OF-PYTHON.git
cd DAY-26-OF-PYTHON
```

### Run the Code
```bash
python day26.py
```

---

## 🌟 Connect & Learn

- **Author**: Harish
- **GitHub**: [@harish-0987](https://github.com/harish-0987)
- **Motto**: *"Not here to be known, here to build."*

Happy Coding! 🚀
