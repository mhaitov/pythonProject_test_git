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

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'


    def __str__(self):
        return f'{self.fullname()}, {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Sam', 'Summers', 1500)
dev2 = Employee('Mary', 'Gold', 2000)

# # Metody dlja ispolzovanija vnutri klassa
# print(repr(emp1))
# print(str(emp1))
# # # same
# # print(emp1.__repr__())
# # print(emp1.__str__())
#
# # Collect solar
# print(emp1 + dev2)

# Dlinna simvolov
print(len(dev2))
print(len(emp1))

