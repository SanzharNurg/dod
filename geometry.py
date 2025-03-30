def get_area(shape, **params):
    """
    Универсальная функция для вычисления площади различных фигур.

    shape (str): Тип фигуры ("rectangle", "square", "circle").
    **params: Аргументы фигуры (ширина, высота, радиус и т.д.).

    Returns:
    float: Площадь фигуры.
    """
    if shape == "rectangle":
        return params["width"] * params["height"]
    elif shape == "square":
        return params["side"] ** 2
    elif shape == "circle":
        return 3.14 * (params["radius"] ** 2)
    else:
        raise ValueError("Неизвестная фигура")
