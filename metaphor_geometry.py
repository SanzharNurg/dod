class ShapeFactory:
    """Фабрика, создающая фигуры (метафора производства)"""

    @staticmethod
    def create_rectangle(width, height):
        return Rectangle(width, height)

    @staticmethod
    def create_square(side):
        return Square(side)


class Shape:
    """Базовый класс для фигур"""

    def area(self):
        raise NotImplementedError("Метод должен быть переопределён в подклассе")


class Rectangle(Shape):
    """Прямоугольник как отдельный класс"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    """Класс Квадрат, наследуется от Shape"""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Использование фабрики (аналогия с производством)
factory = ShapeFactory()
rect = factory.create_rectangle(5, 10)
sq = factory.create_square(4)

print(f"Площадь прямоугольника: {rect.area()}")
print(f"Площадь квадрата: {sq.area()}")
