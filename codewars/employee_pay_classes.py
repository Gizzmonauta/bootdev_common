r"""
This challenge practices classes, methods, and inheritance.

Your task
Build these classes in main.py:

Employee
The Employee class should:

- accept name, hours_worked, and hourly_rate when created
- store those values on the object
- have a get_pay() method that returns total pay
- have a get_summary() method that returns a string in this format:

"Ava earned 120 coins"

Manager
The Manager class should inherit from Employee.

It should:

- accept name, hours_worked, hourly_rate, and bonus when created
- store the bonus
- have a get_pay() method that returns the normal employee pay plus the bonus
- have a get_summary() method that returns a string in this format:

"Manager Bo earned 150 coins"

Example
employee = Employee("Ava", 8, 15)
print(employee.get_pay())
# 120
print(employee.get_summary())
# Ava earned 120 coins

manager = Manager("Bo", 8, 15, 30)
print(manager.get_pay())
# 150
print(manager.get_summary())
# Manager Bo earned 150 coins

Notes
- Manager must use inheritance
- keep pay values as whole numbers in these tests
- main.py should only define classes and values, and should not print anything by itself
"""

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        pass

    def get_pay(self):
        pass

    def get_summary(self):
        pass


class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        pass

    def get_pay(self):
        pass

    def get_summary(self):
        pass