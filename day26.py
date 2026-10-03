# =============================================================================
# DAY 26: OBJECT-ORIENTED PROGRAMMING (OOP) - ENCAPSULATION IN PYTHON
# Author: Harish
# Repository: DAY-26-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

"""
WHAT IS ENCAPSULATION? (BASIC LEVEL GUIDE)
------------------------------------------
Encapsulation is one of the four fundamental pillars of Object-Oriented 
Programming (along with Inheritance, Polymorphism, and Abstraction).

DEFINITION:
  Encapsulation is the mechanism of bundling data (attributes/variables) 
  and the methods (functions) that manipulate that data into a single unit 
  (a class), while simultaneously restricting direct access to some of the 
  object's internal components.

KEY INTUITION & REAL-WORLD ANALOGIES:
  1. Medical Capsule:
     - The capsule encloses diverse medicinal powders inside a protective 
       coating. You consume the capsule as a whole unit without tampering 
       with the individual chemical ingredients inside.
  2. Bank Vault / ATM Machine:
     - You cannot walk into a bank vault and grab money directly.
     - You must use defined public operations: deposit cash, insert card,
       enter a valid PIN, and call withdraw(). The bank securely protects 
       its internal balance.
  3. Smart Phone / Car:
     - You press the gas pedal or touchscreen without needing to manually 
       manipulate engine fuel injection or CPU voltages.

WHY USE ENCAPSULATION?
  1. Data Hiding & Security : Prevents unauthorized or accidental modification 
                              of critical object state.
  2. Data Validation        : Setters enforce business rules before updating 
                              data (e.g., age cannot be negative, deposits > 0).
  3. Read-Only / Write-Only : Control field accessibility using property decorators.
  4. Maintainability        : Internal class implementation can change without 
                              breaking external client code.

ACCESS MODIFIERS IN PYTHON (NAMING CONVENTIONS):
  Unlike languages such as Java or C++ (which use public, protected, private 
  keywords), Python uses naming conventions with underscores:

  | Specifier   | Syntax Example | Accessibility                                    |
  |-------------|----------------|--------------------------------------------------|
  | Public      | `self.name`    | Accessible everywhere (inside & outside class)   |
  | Protected   | `self._salary` | Convention: Accessible inside class & subclasses |
  | Private     | `self.__pin`   | Enforced via Name Mangling: Hidden from outside   |

TOPICS COVERED:
  1. Public Members (Direct Access)
  2. Protected Members (Single Underscore Convention & Subclasses)
  3. Private Members (Double Underscore & Name Mangling)
  4. Traditional Getter & Setter Methods (Controlled Validation)
  5. Pythonic Encapsulation with @property, @setter, and @deleter
  6. Private Helper Methods (Internal Logic Hiding)
  7. Real-World Case Study: Secure Banking & Wallet Management System
"""


def print_section(title: str) -> None:
    """Utility function to print cleanly formatted section headers."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# =============================================================================
# 1. PUBLIC MEMBERS
# =============================================================================
# Public members are accessible freely from inside the class, from derived 
# subclasses, and directly from external code using object instances.
# By default, all attributes and methods in a Python class are public.

class Student:
    """Demonstrates public attributes and public methods."""

    def __init__(self, name: str, roll_no: int):
        self.name = name          # Public attribute
        self.roll_no = roll_no    # Public attribute

    def display_details(self) -> None:
        """Public method."""
        print(f"[Student Info] Name: {self.name} | Roll No: {self.roll_no}")


def demo_public_members():
    print_section("1. PUBLIC MEMBERS (ACCESSIBLE EVERYWHERE)")

    student = Student("Harish", 101)

    print("Initial details via public method:")
    student.display_details()

    print("\nAccessing public attributes directly from outside:")
    print(f"Direct read: student.name    = {student.name}")
    print(f"Direct read: student.roll_no = {student.roll_no}")

    print("\nModifying public attributes directly:")
    student.name = "Harish Kumar"
    student.roll_no = 102
    student.display_details()
    print(">> Note: Public members have zero restrictions or validation.")


# =============================================================================
# 2. PROTECTED MEMBERS (_single_underscore)
# =============================================================================
# Python does not have a strict 'protected' keyword. Instead, PEP 8 defines
# a single leading underscore `_attribute` as a convention.
# It indicates: "This member is intended for internal use within this class
# and its subclasses. Please do NOT modify it directly from the outside."

class Company:
    """Base class demonstrating protected members."""

    def __init__(self, company_name: str, founded_year: int):
        self.company_name = company_name   # Public
        self._founded_year = founded_year  # Protected member (by convention)

    def _internal_audit_code(self) -> str:
        """Protected method."""
        return f"AUDIT-{self._founded_year}-XYZ"


class Branch(Company):
    """Subclass accessing protected members of the parent class."""

    def __init__(self, company_name: str, founded_year: int, branch_city: str):
        super().__init__(company_name, founded_year)
        self.branch_city = branch_city  # Public

    def display_branch_summary(self) -> None:
        # Accessing protected member `_founded_year` and method `_internal_audit_code`
        print(f"Company: {self.company_name} ({self.branch_city} Branch)")
        print(f"Founded Year (Protected access in Subclass): {self._founded_year}")
        print(f"Audit Code   (Protected method in Subclass): {self._internal_audit_code()}")


def demo_protected_members():
    print_section("2. PROTECTED MEMBERS (CONVENTION: _single_underscore)")

    branch = Branch("TechCorp Solutions", 2018, "Bengaluru")
    branch.display_branch_summary()

    print("\nCan outside code still access a protected member in Python?")
    print(f"Direct outside read: branch._founded_year = {branch._founded_year}")
    print(">> Important: Python does NOT physically block access to single underscores.")
    print(">> It is a gentleman's agreement: developers must treat it as protected!")


# =============================================================================
# 3. PRIVATE MEMBERS (__double_underscore) & NAME MANGLING
# =============================================================================
# Attributes prefixed with two leading underscores (and at most one trailing)
# e.g., `__attribute` are PRIVATE to the class.
# Python enforces privacy using NAME MANGLING:
#   Python internally renames `__balance` to `_ClassName__balance`.
#   This prevents accidental access or overriding from outside or derived classes.

class SafeBox:
    """Class with private attributes and private methods."""

    def __init__(self, owner: str, secret_code: str):
        self.owner = owner                # Public
        self.__secret_code = secret_code  # Private attribute

    def reveal_secret(self, entered_password: str) -> None:
        """Public method providing authorized access to private attribute."""
        if entered_password == "admin123":
            print(f"Access Granted! Secret Code: {self.__secret_code}")
        else:
            print("Access Denied! Incorrect password.")


def demo_private_members():
    print_section("3. PRIVATE MEMBERS (__double_underscore) & NAME MANGLING")

    box = SafeBox("Harish", "CLASSIFIED-9988")

    print(f"Public owner: {box.owner}")

    # Attempting direct access to private attribute:
    print("\nAttempting direct outside access: box.__secret_code ...")
    try:
        print(box.__secret_code)
    except AttributeError as err:
        print(f">> Caught Expected Error: {err}")
        print(">> Direct outside access is blocked by Python!")

    print("\nAccessing through authorized public method:")
    box.reveal_secret("wrong_pass")
    box.reveal_secret("admin123")

    print("\nUnderstanding Name Mangling:")
    print("Python renames `__secret_code` to `_SafeBox__secret_code` behind the scenes:")
    mangled_name = "_SafeBox__secret_code"
    print(f"Direct read via mangled name: getattr(box, '{mangled_name}') = {getattr(box, mangled_name)}")
    print(">> Note: Name mangling prevents collisions, but encapsulation requires")
    print("   respecting class boundaries rather than hacking mangled names.")


# =============================================================================
# 4. TRADITIONAL GETTERS & SETTERS (VALIDATION)
# =============================================================================
# Getters (Accessors) and Setters (Mutators) provide controlled entry points
# to inspect and update private attributes while performing input validation.

class Employee:
    """Demonstrates traditional getter and setter methods with validation."""

    def __init__(self, emp_name: str, base_salary: float):
        self.emp_name = emp_name          # Public
        self.__salary = 0.0               # Private
        self.set_salary(base_salary)      # Use setter for initial validation

    # Getter for salary
    def get_salary(self) -> float:
        """Returns the private salary."""
        return self.__salary

    # Setter for salary with business rules
    def set_salary(self, new_salary: float) -> None:
        """Validates and updates the private salary."""
        if not isinstance(new_salary, (int, float)):
            raise TypeError("Salary must be a numerical value!")
        if new_salary <= 0:
            print(f"Error: Invalid salary ${new_salary}. Salary must be positive!")
            return
        if new_salary < 1000:
            print(f"Error: ${new_salary} is below minimum wage ($1000).")
            return

        self.__salary = float(new_salary)
        print(f"Salary successfully updated to: ${self.__salary:,.2f}")


def demo_traditional_getters_setters():
    print_section("4. TRADITIONAL GETTER & SETTER METHODS WITH VALIDATION")

    emp = Employee("Alex Turner", 3500.0)
    print(f"Employee Name : {emp.emp_name}")
    print(f"Current Salary: ${emp.get_salary():,.2f}")

    print("\nAttempting invalid salary updates:")
    emp.set_salary(-500)     # Rejected: negative
    emp.set_salary(400)      # Rejected: below minimum wage

    print("\nAttempting valid salary update:")
    emp.set_salary(5200.0)   # Accepted
    print(f"Updated Salary via get_salary(): ${emp.get_salary():,.2f}")


# =============================================================================
# 5. PYTHONIC ENCAPSULATION WITH @property DECORATOR
# =============================================================================
# Python provides the `@property` decorator to make methods act like attributes.
# This allows clean, pythonic syntax (`obj.temperature = 25`) while secretly
# running getter, setter, and deleter validation under the hood!

class TemperatureSensor:
    """
    Demonstrates Pythonic encapsulation:
      - @property for getter
      - @celsius.setter for setter with validation
      - Read-only property (fahrenheit has getter only)
    """

    def __init__(self, celsius: float):
        self._celsius = 0.0          # Protected backing field
        self.celsius = celsius       # Triggers @celsius.setter validation

    # 1. Getter
    @property
    def celsius(self) -> float:
        """Getter for celsius."""
        return self._celsius

    # 2. Setter with validation
    @celsius.setter
    def celsius(self, value: float) -> None:
        """Validates temperature does not go below absolute zero (-273.15 C)."""
        if value < -273.15:
            raise ValueError(f"Temperature {value} C is below Absolute Zero (-273.15 C)!")
        self._celsius = float(value)

    # 3. Read-Only Property (Calculated on the fly, no setter provided!)
    @property
    def fahrenheit(self) -> float:
        """Calculates Fahrenheit from Celsius on demand. Read-only."""
        return (self._celsius * 9 / 5) + 32

    # 4. Deleter
    @celsius.deleter
    def celsius(self) -> None:
        """Deleter resets sensor to baseline."""
        print("Resetting sensor value to 0.0 C...")
        self._celsius = 0.0


def demo_property_decorator():
    print_section("5. PYTHONIC ENCAPSULATION: @property, @setter, @deleter")

    sensor = TemperatureSensor(25.0)
    print(f"Read Celsius via property    : {sensor.celsius} C")
    print(f"Read Fahrenheit (calculated)  : {sensor.fahrenheit:.1f} F")

    print("\nModifying temperature using normal attribute assignment syntax:")
    sensor.celsius = 37.5
    print(f"New Celsius   : {sensor.celsius} C")
    print(f"New Fahrenheit: {sensor.fahrenheit:.1f} F")

    print("\nAttempting to assign directly to read-only property 'fahrenheit':")
    try:
        # fahrenheit has no setter defined, so this will raise AttributeError
        sensor.fahrenheit = 100.0  # type: ignore
    except AttributeError as err:
        print(f">> Caught Expected Error: {err}")
        print(">> 'fahrenheit' is protected as a READ-ONLY property!")

    print("\nAttempting invalid assignment below absolute zero:")
    try:
        sensor.celsius = -300.0
    except ValueError as err:
        print(f">> Caught Expected Validation Error: {err}")

    print("\nUsing deleter:")
    del sensor.celsius
    print(f"Celsius after deletion: {sensor.celsius} C")


# =============================================================================
# 6. PRIVATE HELPER METHODS (INTERNAL LOGIC HIDING)
# =============================================================================
# Encapsulation applies to methods too!
# Internal implementation details and sensitive algorithms should be private
# helper methods (`__method_name`), exposing only clean public interfaces.

class EmailService:
    """Demonstrates private helper methods."""

    def __init__(self, sender_email: str):
        self.sender_email = sender_email

    # Private Helper 1: Sanitize text
    def __sanitize_content(self, text: str) -> str:
        """Internal helper to clean whitespace and escape characters."""
        return text.strip()

    # Private Helper 2: Simulated SMTP Handshake
    def __authenticate_smtp(self) -> bool:
        """Simulate internal authentication."""
        return True

    # Public Interface
    def send_email(self, recipient: str, body: str) -> bool:
        """Public method that coordinates internal private steps."""
        if "@" not in recipient:
            print(f"Error: Invalid recipient address '{recipient}'.")
            return False

        if not self.__authenticate_smtp():
            print("Error: SMTP Handshake failed.")
            return False

        clean_body = self.__sanitize_content(body)
        print(f"Email successfully dispatched to {recipient}!")
        print(f"Message preview: '{clean_body}'")
        return True


def demo_private_methods():
    print_section("6. PRIVATE HELPER METHODS (INTERNAL LOGIC HIDING)")

    service = EmailService("noreply@mycloudapp.com")
    print("Calling clean public API: service.send_email(...)")
    service.send_email("harish.developer@example.com", "   Hello, Welcome to Day 26!   ")

    print("\nAttempting to call private helper method directly:")
    try:
        service.__authenticate_smtp()  # type: ignore
    except AttributeError as err:
        print(f">> Caught Expected Error: {err}")
        print(">> Internal implementation details remain safely hidden.")


# =============================================================================
# 7. REAL-WORLD COMPREHENSIVE PROJECT: SECURE BANK ACCOUNT & SMART WALLET
# =============================================================================
# A full-scale demonstration combining:
#   - Public: Account holder name, account type
#   - Read-only property: Account number
#   - Protected: Account tier (_tier)
#   - Private: Balance (__balance), PIN (__pin), Transaction History (__transactions)
#   - Methods: deposit(), withdraw(), check_balance(), change_pin(), mini_statement()

import datetime


class BankAccount:
    """
    Production-grade example of Encapsulation in Banking.
    Protects user funds, validates credentials, logs immutable transactions.
    """

    def __init__(self, account_number: str, holder_name: str, initial_deposit: float, pin: int):
        self.holder_name = holder_name                    # Public
        self.account_type = "Savings"                     # Public
        self._tier = "Gold" if initial_deposit >= 5000 else "Standard"  # Protected
        
        self.__account_number = account_number            # Private (Read-only property)
        self.__pin = pin                                  # Private (Strictly hidden)
        self.__balance = 0.0                              # Private
        self.__transaction_history: list[dict] = []       # Private ledger

        if initial_deposit < 500:
            raise ValueError("Minimum initial opening deposit is $500.00!")

        self.__balance = float(initial_deposit)
        self.__record_transaction("OPENING_DEPOSIT", initial_deposit, self.__balance)

    # --- Read-Only Property for Account Number ---
    @property
    def account_number(self) -> str:
        """Public read-only masked account number."""
        # Displays masked account number e.g. *******1234
        return f"*******{self.__account_number[-4:]}"

    # --- Read-Only Property for Balance (requires no pin for display if needed) ---
    @property
    def account_tier(self) -> str:
        """Public read-only account tier."""
        return self._tier

    # --- Private Helper Methods ---
    def __verify_pin(self, entered_pin: int) -> bool:
        """Internal private method to authenticate transactions."""
        return self.__pin == entered_pin

    def __record_transaction(self, tx_type: str, amount: float, balance_after: float) -> None:
        """Internal private method to write to immutable audit log."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "time": timestamp,
            "type": tx_type,
            "amount": amount,
            "balance": balance_after
        }
        self.__transaction_history.append(record)

    # --- Public API Methods ---
    def check_balance(self, pin: int) -> float | None:
        """Secure balance inquiry with PIN verification."""
        if not self.__verify_pin(pin):
            print("[Alert] Incorrect PIN! Access to balance inquiry denied.")
            return None
        print(f"[Balance Inquiry] Current balance: ${self.__balance:,.2f}")
        return self.__balance

    def deposit(self, amount: float) -> bool:
        """Public deposit method with positive amount validation."""
        if amount <= 0:
            print("[Deposit Error] Deposit amount must be greater than $0.00!")
            return False

        self.__balance += amount
        self.__record_transaction("DEPOSIT", amount, self.__balance)
        print(f"[Deposit Success] Added ${amount:,.2f}. New Balance: ${self.__balance:,.2f}")
        return True

    def withdraw(self, amount: float, pin: int) -> bool:
        """Secure withdrawal with validation against funds and PIN."""
        if not self.__verify_pin(pin):
            print("[Withdraw Error] Authentication failed: Incorrect PIN.")
            return False

        if amount <= 0:
            print("[Withdraw Error] Withdrawal amount must be greater than $0.00.")
            return False

        if amount > self.__balance:
            print(f"[Withdraw Error] Insufficient funds! Requested ${amount:,.2f}, Available ${self.__balance:,.2f}")
            return False

        self.__balance -= amount
        self.__record_transaction("WITHDRAWAL", amount, self.__balance)
        print(f"[Withdraw Success] Withdrawn ${amount:,.2f}. Remaining Balance: ${self.__balance:,.2f}")
        return True

    def change_pin(self, current_pin: int, new_pin: int) -> bool:
        """Allows user to update PIN with verification and format validation."""
        if not self.__verify_pin(current_pin):
            print("[Security Error] Current PIN verification failed.")
            return False

        if not (1000 <= new_pin <= 9999):
            print("[Security Error] New PIN must be exactly 4 digits (1000 - 9999).")
            return False

        self.__pin = new_pin
        print("[Security Success] PIN updated successfully!")
        return True

    def print_mini_statement(self, pin: int) -> None:
        """Prints formatted statement of recent transactions."""
        if not self.__verify_pin(pin):
            print("[Security Error] Access denied: PIN verification required for statement.")
            return

        print("\n" + "-" * 65)
        print(f" MINI-STATEMENT: {self.holder_name} ({self.account_number})")
        print(f" Tier: {self._tier} | Available Balance: ${self.__balance:,.2f}")
        print("-" * 65)
        print(f"{'Timestamp':<20} | {'Type':<15} | {'Amount':<10} | {'Balance'}")
        print("-" * 65)
        for tx in self.__transaction_history:
            print(f"{tx['time']:<20} | {tx['type']:<15} | ${tx['amount']:<9.2f} | ${tx['balance']:,.2f}")
        print("-" * 65)


def demo_banking_case_study():
    print_section("7. REAL-WORLD CASE STUDY: SECURE BANK ACCOUNT & ENCAPSULATION")

    # Creating account
    account = BankAccount("987654321098", "Harish", 6000.0, 4321)

    print(f"Account Holder : {account.holder_name}")
    print(f"Masked Number  : {account.account_number}")
    print(f"Account Tier   : {account.account_tier}")

    print("\n--- Testing Deposits ---")
    account.deposit(1500.0)
    account.deposit(-200.0)  # Invalid deposit rejected

    print("\n--- Testing Withdrawals ---")
    account.withdraw(500.0, 9999)    # Wrong PIN
    account.withdraw(10000.0, 4321)  # Overdraft rejected
    account.withdraw(1200.0, 4321)   # Successful withdrawal

    print("\n--- Testing PIN Change ---")
    account.change_pin(4321, 8888)

    print("\n--- Verifying Direct Access Protection ---")
    try:
        print(account.__balance)  # type: ignore
    except AttributeError:
        print(">> Confirmed: Direct balance access is strictly prevented!")

    print("\n--- Viewing Account Statement ---")
    account.print_mini_statement(8888)


# =============================================================================
# SUMMARY TABLE
# =============================================================================

def print_encapsulation_summary():
    print_section("ENCAPSULATION COMPARISON MATRIX")
    table = """
| Type        | Notation           | Outside Access | Subclass Access | Purpose                                |
|-------------|--------------------|----------------|-----------------|----------------------------------------|
| Public      | self.name          | Yes (Direct)   | Yes (Inherited) | General data and interface methods     |
| Protected   | self._salary       | Conventionally | Yes             | Internal state, extensible by children |
| Private     | self.__balance     | No (Name Mangle)| No (Mangled)   | Critical state & sensitive validation  |
| Property    | @property          | Controlled     | Yes             | Pythonic getters/setters/validation    |
"""
    print(table.strip())


# =============================================================================
# MAIN ENTRYPOINT
# =============================================================================

def main() -> None:
    print("=" * 70)
    print(" DAY 26: OBJECT-ORIENTED PROGRAMMING (OOP) - ENCAPSULATION IN PYTHON")
    print(" Author: Harish | Repository: DAY-26-OF-PYTHON")
    print(" Motto: 'Not here to be known, here to build.'")
    print("=" * 70)

    demo_public_members()
    demo_protected_members()
    demo_private_members()
    demo_traditional_getters_setters()
    demo_property_decorator()
    demo_private_methods()
    demo_banking_case_study()
    print_encapsulation_summary()

    print("\n" + "=" * 70)
    print(" DAY 26 COMPLETE: Encapsulation in Python Mastered Successfully!")
    print(" 'Not here to be known, here to build.'")
    print("=" * 70)


if __name__ == "__main__":
    main()
