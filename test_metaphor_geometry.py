
from metaphor_geometry import ShapeFactory, Rectangle, Square

def test_rectangle_area():
    rect = Rectangle(5, 10)
    assert rect.area() == 50

def test_square_area():
    sq = Square(4)
    assert sq.area() == 16

def test_factory_creates_rectangle():
    factory = ShapeFactory()
    rect = factory.create_rectangle(3, 6)
    assert isinstance(rect, Rectangle)
    assert rect.area() == 18

def test_factory_creates_square():
    factory = ShapeFactory()
    sq = factory.create_square(5)
    assert isinstance(sq, Square)
    assert sq.area() == 25
