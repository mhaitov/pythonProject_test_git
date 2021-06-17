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
        # self.email = first.lower() + '.' + last.lower() + '@company.com'
        # Employee.num_of_employees += 1

    @property
    def email(self):
        return self.first.lower() + '.' + self.last.lower() + '@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting name!')
        self.first = None
        self.last = None



emp1 = Employee('Sam', 'Summers', 2000)
dev2 = Employee('Mary', 'Gold', 2500)

print(emp1.first)
print(emp1.email)

print(emp1.__dict__)
emp1.fullname = 'Jack Green'
print(emp1.__dict__)

del emp1.fullname
print(emp1.__dict__)
