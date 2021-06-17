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
