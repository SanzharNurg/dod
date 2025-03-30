def calculate_area(shape, **params):
    if shape == "rectangle":
        return params["width"] * params["height"]
    elif shape == "circle":
        from math import pi
        return pi * (params["radius"] ** 2)
    else:
        raise ValueError("Unsupported shape")

def calculate_perimeter(shape, **params):
    if shape == "rectangle":
        return 2 * (params["width"] + params["height"])
    elif shape == "circle":
        from math import pi
        return 2 * pi * params["radius"]
    else:
        raise ValueError("Unsupported shape")
