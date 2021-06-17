##### INIT (inicialization)
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

    # Class method
    @classmethod
    def set_pay_raise(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, pay, = string.split('-')
        return cls(first, last, pay)

    # Static method
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday() == 6:
            return  False
        return True



# # print(Employee.num_of_employees)
# # emp1 = Employee('John', 'Smith', 2000)
# # print(Employee.num_of_employees)
# # emp2 = Employee('Mary', 'Gold', 2500)
# # print(Employee.num_of_employees)
# # # # # # print(emp1.email)
# # # # # # print(emp2.email)
# # # # # # print(f'{emp1.first} {emp1.last}')
# # # # # print(emp1.Fullname())
# # # # # print(emp2.Fullname())
# # # # #
# # # # # print(Employee.Fullname(emp1))
# # # # # print(Employee.Fullname(emp2))
# # # #
# # # # print(emp1.pay)
# # # # emp1.pay_raise()
# # # # print(emp1.pay)
# # #
# # # print(emp1.__dict__)
# # # print(Employee.__dict__)
# # #
# # # emp1.pay_raise()
# # # print(emp1.pay)
# # # Employee.raise_amount = 1.06
# # # emp1.pay_raise()
# # # print(emp1.pay)
# # # print(emp1.__dict__)
# # # print(Employee.__dict__)
#
# emp1 = Employee('John', 'Smith', 2000)
# emp2 = Employee('Mary', 'Gold', 2500)
#
# print(emp1.raise_amount)
# print(Employee.raise_amount)
# print(emp1.__dict__)
# emp1.raise_amount = 1.08
# Employee.set_pay_raise(1.10)
# print(emp1.__dict__)
# print(emp1.raise_amount)
# print(Employee.raise_amount)
#

emp1 = Employee('John', 'Smith', 2000)
emp2 = Employee('Mary', 'Gold', 2500)
#
# emp_str_1 = 'Bob-Morgan-1500'
# emp2_str_2 = 'Jack-Summers-2000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.fullname())
# print(new_emp_1.email)

my_date = datetime.date(2021, 4, 16)
print(Employee.is_workday(my_date))


