# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def name(self):
#         print(f"Point ({self.x} {self.y})")


# Point.default_color = "yellow"

# point = Point(1, 2)
# print(point.default_color)
# print(Point.default_color)
# point.name()

# another = Point(3, 4)
# print(another.default_color)
# another.name()

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(6, 0)

#     def name(self):
#         print(f"Point ({self.x} {self.y})")


# point = Point.zero()
# point.name()


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x} {self.y})"

#     def name(self):
#         print(f"name is ({self.x} {self.y})")


# point = Point(1, 2)

# print(str(point))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# point = Point(1, 2)
# other = Point(1, 2)

# print(point == other)

# ========== inheritance =============

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def walk(self):
#         print("Walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")


# m = Fish()
# m.eat()
# print(m.age)\

# ========= multiple inheritance=============

# class InvalidOperationError(Exception):
#     pass


# class Stream:

#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened.")

#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already Closed.")

#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a Network")


# stream = FileStream()


# ======== abstract based clasees ==================
# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):

#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened.")

#         self.opened = True
#         print("Stream opened")

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already Closed.")

#         self.opened = False
#         print("Stream closed")

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a Network")


# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a  memory stream.")


# stream = MemoryStream()
# stream.read()


def make_sound(animal):
    animal.sound()   # Python only cares: "Does this object have a sound() method?"


class Cow:
    def sound(self):
        print("Moo")


class Fish:
    def swim(self):
        print("Swimming")


make_sound(Cow())   # ✅ Works, Cow has sound()
make_sound(Fish())  # ❌ ERROR, Fish does NOT have sound()
