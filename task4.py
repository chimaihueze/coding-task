import math
import logging
from abc import ABC, abstractmethod

# LOGGING SETUP
logging.basicConfig(
    filename='task4.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class Shape(ABC):
    def __init__(self, name) -> None:
        logging.debug(f"Initializing Shape with name: {name}")
        self.name = name

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def surface_area(self):
        pass

    def __str__(self):
        try:
            description = f"{self.name} - Perimeter: {self.perimeter:.2f}, Surface Area: {self.surface_area:.2f}"
            logging.debug(f"String representation of Shape: {description}")
            return description
        except Exception as e:
            logging.error(f"Error in __str__ method of Shape: {e}")
            raise


class Circle(Shape):
    def __init__(self, radius):
        logging.debug(f"Initializing Circle with radius: {radius}")
        super().__init__("Circle")
        self.radius = radius

    @property
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        logging.debug(f"Calculated perimeter of Circle: {perimeter}")
        return perimeter

    @property
    def surface_area(self):
        surface_area = math.pi * self.radius ** 2
        logging.debug(f"Calculated surface area of Circle: {surface_area}")
        return surface_area


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        name = self.determine_name(side1, side2, side3)
        logging.debug(f"Initializing Triangle with sides: {side1}, {side2}, {side3}, Name: {name}")
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        logging.debug(f"Calculated perimeter of Triangle: {perimeter}")
        return perimeter

    @property
    def surface_area(self):
        s = self.perimeter / 2
        surface_area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        logging.debug(f"Calculated surface area of Triangle: {surface_area}")
        return surface_area

    @staticmethod
    def determine_name(side1, side2, side3):
        name = (
            "Equilateral Triangle" if side1 == side2 == side3 else
            "Isosceles Triangle" if side1 == side2 or side2 == side3 or side1 == side3 else
            "Scalene Triangle"
        )
        logging.debug(f"Determined name of Triangle: {name}")
        return name


class Rectangle(Shape):
    def __init__(self, width, height):
        logging.debug(f"Initializing Rectangle with width: {width}, height: {height}")
        super().__init__("Rectangle")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        logging.debug(f"Calculated perimeter of Rectangle: {perimeter}")
        return perimeter

    @property
    def surface_area(self):
        surface_area = self.width * self.height
        logging.debug(f"Calculated surface area of Rectangle: {surface_area}")
        return surface_area


circle = Circle(radius=5)
triangle = Triangle(side1=3, side2=4, side3=5)
rectangle = Rectangle(width=4, height=6)

print(circle)
print(triangle)
print(rectangle)
