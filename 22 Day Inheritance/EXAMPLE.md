In object-oriented programming (OOP), inheritance is a mechanism where one class (child class) inherits the properties and behaviors (methods) of another class (parent class). This helps reduce redundancy, improves code reusability, and makes the system easier to maintain.

### Types of Inheritance
There are different types of inheritance, which are classified based on how classes relate to each other. Let’s go through the basic types using a simple bank example:

1. **Single Inheritance**
   - In single inheritance, a subclass (child class) inherits from one superclass (parent class).
   - Example:
     ```python
     class BankAccount:
         def __init__(self, account_holder, balance):
             self.account_holder = account_holder
             self.balance = balance

         def deposit(self, amount):
             self.balance += amount

         def withdraw(self, amount):
             if self.balance >= amount:
                 self.balance -= amount
             else:
                 print("Insufficient funds")

     class SavingsAccount(BankAccount):
         def __init__(self, account_holder, balance, interest_rate):
             super().__init__(account_holder, balance)  # Inherit attributes from BankAccount
             self.interest_rate = interest_rate

         def calculate_interest(self):
             return self.balance * (self.interest_rate / 100)

     # Usage
     savings_account = SavingsAccount("John", 1000, 5)
     print(savings_account.calculate_interest())  # 50.0
     ```

   - **Explanation:**
     - `SavingsAccount` inherits from the `BankAccount` class.
     - The `SavingsAccount` class has additional attributes like `interest_rate` and a method `calculate_interest`.
     - It uses `super()` to call the constructor of the parent class (`BankAccount`) to initialize `account_holder` and `balance`.

2. **Multilevel Inheritance**
   - In multilevel inheritance, a class is derived from another derived class.
   - Example:
     ```python
     class BankAccount:
         def __init__(self, account_holder, balance):
             self.account_holder = account_holder
             self.balance = balance

         def deposit(self, amount):
             self.balance += amount

     class SavingsAccount(BankAccount):
         def __init__(self, account_holder, balance, interest_rate):
             super().__init__(account_holder, balance)
             self.interest_rate = interest_rate

         def calculate_interest(self):
             return self.balance * (self.interest_rate / 100)

     class PremiumSavingsAccount(SavingsAccount):
         def __init__(self, account_holder, balance, interest_rate, reward_points):
             super().__init__(account_holder, balance, interest_rate)
             self.reward_points = reward_points

         def redeem_points(self):
             return self.reward_points * 10  # Each point worth 10 units
         
     # Usage
     premium_account = PremiumSavingsAccount("Alice", 2000, 3, 150)
     print(premium_account.redeem_points())  # 1500
     ```

   - **Explanation:**
     - `PremiumSavingsAccount` inherits from `SavingsAccount`, which in turn inherits from `BankAccount`.
     - `PremiumSavingsAccount` gets both the deposit functionality from `BankAccount` and interest calculation from `SavingsAccount`.

3. **Multiple Inheritance**
   - Multiple inheritance is when a class inherits from more than one parent class.
   - Example:
     ```python
     class BankAccount:
         def __init__(self, account_holder, balance):
             self.account_holder = account_holder
             self.balance = balance

         def deposit(self, amount):
             self.balance += amount

     class LoanAccount:
         def __init__(self, loan_amount, loan_interest):
             self.loan_amount = loan_amount
             self.loan_interest = loan_interest

         def calculate_loan_interest(self):
             return self.loan_amount * (self.loan_interest / 100)

     class PersonalAccount(BankAccount, LoanAccount):
         def __init__(self, account_holder, balance, loan_amount, loan_interest):
             BankAccount.__init__(self, account_holder, balance)
             LoanAccount.__init__(self, loan_amount, loan_interest)

     # Usage
     personal_account = PersonalAccount("Sam", 5000, 10000, 5)
     print(personal_account.calculate_loan_interest())  # 500.0
     ```

   - **Explanation:**
     - `PersonalAccount` inherits from both `BankAccount` and `LoanAccount`.
     - It can access the methods and properties from both parent classes.

4. **Hierarchical Inheritance**
   - In hierarchical inheritance, multiple subclasses inherit from a single parent class.
   - Example:
     ```python
     class BankAccount:
         def __init__(self, account_holder, balance):
             self.account_holder = account_holder
             self.balance = balance

         def deposit(self, amount):
             self.balance += amount

     class SavingsAccount(BankAccount):
         def __init__(self, account_holder, balance, interest_rate):
             super().__init__(account_holder, balance)
             self.interest_rate = interest_rate

         def calculate_interest(self):
             return self.balance * (self.interest_rate / 100)

     class CheckingAccount(BankAccount):
         def __init__(self, account_holder, balance, overdraft_limit):
             super().__init__(account_holder, balance)
             self.overdraft_limit = overdraft_limit

         def check_overdraft(self):
             if self.balance < 0:
                 return f"Overdraft limit exceeded! Limit: {self.overdraft_limit}"
             return "Within limit"

     # Usage
     savings_account = SavingsAccount("Eve", 2000, 4)
     checking_account = CheckingAccount("Bob", 500, 100)

     print(savings_account.calculate_interest())  # 80.0
     print(checking_account.check_overdraft())  # Within limit
     ```

   - **Explanation:**
     - Both `SavingsAccount` and `CheckingAccount` inherit from `BankAccount`.
     - Each class adds its own specialized methods.

### Conclusion

- **Single inheritance** allows one class to inherit from another.
- **Multilevel inheritance** forms a chain of inheritance.
- **Multiple inheritance** enables a class to inherit from multiple classes.
- **Hierarchical inheritance** allows multiple classes to inherit from a single parent.

Inheritance in OOP promotes code reuse and helps create a clear and manageable structure for complex programs.
