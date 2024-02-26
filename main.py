# class Geom:
#     name = "Geom"
#
#     def set_coords(self, x1, y1, z1):
#         print(self)
#         self.x1 = x1
#         self.y1 = y1
#         self.z1 = z1
#         self.draw()
#
#     def draw(self):
#         print("Draw geom")
#
# class Line(Geom):
#     name = "Line"
#
#     def draw(self):
#         print("Draw line")
#
# class Rect(Geom):
#     name = "Rect"
#
#     def draw(self):
#         print("Draw rect")
#
# geom = Geom()
# print(geom.name)
#
# line = Line()
# # line.draw()
# print(line.name)
# geom.draw()
# line.draw()
# rect = Rect()
# rect.set_coords(1, 2, 3)
# line.set_coords(1, 2, 3)
# geom.set_coords(1, 2, 3)
#
# line.set_name("General")
# print(line.name)
# print(Line.name)
# print(geom.name)

# class Geom:
#     pass
#
# class Line(Geom):
#     pass
#
# geom = Geom()
# line = Line()
# print(issubclass(dict, object))
# print(isinstance(geom, object))
#
# bool

# class Vector(list):
#     pass
#     # def __str__(self):
#     #     return ", ".join(map(str, self))
#
#
# vector = Vector([1, 2, 3, 4])
# print(vector)

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
