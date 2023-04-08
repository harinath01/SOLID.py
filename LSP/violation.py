# Example 1
class Vehicle:
    """A demo Vehicle class"""

    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        """Get vehicle name"""
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        """Get vehicle speed"""
        return f"The vehicle speed {self.speed}"

    def engine(self):
        """A vehicle engine"""
        pass

    def start_engine(self):
        """A vehicle engine start"""
        self.engine()


class Car(Vehicle):
    """A demo Car Vehicle class"""

    def start_engine(self):
        pass


class Bicycle(Vehicle):
    """A demo Bicycle Vehicle class"""

    def start_engine(self):
        pass

# Example 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height