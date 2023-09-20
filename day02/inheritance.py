"""
Inheritance in Python is similar to inheritance in Java
Python SUPPORTS Multiple Inheritance (unlike Java)
The default constructor of a subClass is the parent (super) const (In Java the default const is No-Args Const)
"""

class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):

    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age)
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')


class Developer(Employee):

    def __init__(self, name: str, age: int, job_title: str = 'Developer', company_name: str = 'Unknown', salary: int = 0, prgramming_lang: str = ''):
        super().__init__(name, age, job_title, company_name, salary)
        self.programming_lang = prgramming_lang

    # Overriden method
    def work(self):
        print(f'{self.job_title}, {self.name}... is coding')

employee1 = Employee("Kari", 32, 'QA')
developer1= Developer("Zack", 42, 'Java Developer', 'Google', 190000, 'Java, Python, C#')

print(employee1)
print(developer1)
print('-------------------------------')
employee1.work()
developer1.work()





