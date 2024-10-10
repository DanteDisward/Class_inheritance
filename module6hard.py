import math


class Figure:
    def __init__(self, color, sides, filled=False):
        self.__sides = sides
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(0, 255) and g in range(0, 255) and b in range(0, 255):
            result = True
        else:
            result = False
        return result

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        if isinstance(sides, int) and sides > 0:
            result = True
        else:
            result = False
        return result

    def get_sides(self):
        return self.__sides

    def __len__(self):
        result = 0
        for i in self.__sides:
            result += i
        return result

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        return self.__sides

    sides_count = 0


class Circle(Figure):
    def __init__(self, color, *sides, filled=False):
        sides1 = []
        if len(sides) == 1:
            sides1.append(sides[0])
        else:
            sides1.append(1)
        super().__init__(color, sides1, filled)
        self.__radius = sides1[0] / (2 * math.pi)

    def get_square(self):
        result = math.pi * (self.__radius ** 2)
        return result

    sides_count = 1


class Triangle(Figure):
    def __init__(self, color, *sides, filled=False):
        sides1 = []
        if len(sides) == 3:
            sides1 = list(sides)
        else:
            for i in range(0, 3):
                sides1.append(1)
        super().__init__(color, sides1, filled)

    def get_square(self):
        a = super().set_sides()[0]
        b = super().set_sides()[1]
        c = super().set_sides()[2]
        p = 0.5 * (a + b + c)
        result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return result

    sides_count = 3


class Cube(Figure):
    def __init__(self, color, *sides, filled=False):
        sides1 = []
        if len(sides) == 1:
            self.len_cube = sides[0]
            for i in range(0, 12):
                sides1.append(sides[0])
        else:
            for i in range(0, 12):
                sides1.append(1)
        super().__init__(color, sides1, filled)

    def get_volume(self):
        result = super().set_sides()[0] ** 3
        return result

    sides_count = 12


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 35, 130), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
triangle1.set_color(22, 22, 22)
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
triangle1.set_sides(5)
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

print(cube1.get_volume())  # Объём куба
print(circle1.get_square())  # Площадь круга
print(triangle1.get_square())  # Площадь треугольника
