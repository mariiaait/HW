class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"Name: {self._name} Age: {self._age}"


class Employee(Person):
    def __init__(self, name, age, company, position):
        super().__init__(name, age)
        self._company = company
        self._position = position

    def __str__(self):
        return f"{super().__str__()} Company: {self._company} Position: {self._position}"


employee = Employee("Tom", 25, "Google", "Developer")
print(employee)