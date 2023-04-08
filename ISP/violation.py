# Example 1
class Shape:
    """A demo shape class"""

    def draw_circle(self):
        """Draw a circle"""
        raise NotImplemented

    def draw_square(self):
        """ Draw a square"""
        raise NotImplemented


class Circle(Shape):
    """A demo circle class"""


def draw_circle(self):
    """Draw a circle"""
    pass


def draw_square(self):
    """ Draw a square"""
    pass

# Example 2
class Document:
    def __init__(self, name):
        self.name = name

    def open(self):
        pass

    def close(self):
        pass

    def save(self):
        pass


class Word(Document):
    def open(self):
        # Implement Word-specific open functionality
        pass

    def close(self):
        # Implement Word-specific close functionality
        pass

    def save(self):
        # Implement Word-specific save functionality
        pass

    def print(self):
        # Implement Word-specific print functionality
        pass


class Excel(Document):
    def open(self):
        # Implement Excel-specific open functionality
        pass

    def close(self):
        # Implement Excel-specific close functionality
        pass

    def save(self):
        # Implement Excel-specific save functionality
        pass

    def export_pdf(self):
        # Implement Excel-specific export to PDF functionality
        pass