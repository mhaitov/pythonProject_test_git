import datetime
class Employee:

    # Class variables
    num_of_employees = 0
    raise_amount = 1.04

    # Regular variables
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def pay_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)  #same like (self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang='Nothing'):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


#
# emp1 = Developer('John', 'Smith', 2000, 'Python')
# emp2 = Developer('Mary', 'Gold', 2500, 'C#')

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp1 = Employee('Sam', 'Summers', 2000,)

dev1 = Developer('John', 'Smith', 2000, 'Python')
dev2 = Developer('Mary', 'Gold', 2500, 'C#')

#
# print(emp1.pay)
# print(dev1.pay)
# emp1.pay_raise()
# dev1.pay_raise()
# print(emp1.pay)
# print(dev1.pay)

man1 = Manager('Simon', 'Green', 5000, [dev1])
man1.print_employee()
print('\n')
man1.add_employee(dev1)
man1.print_employee()
print('\n')
man1.remove_employee(dev1)
man1.print_employee()

