from geometry import get_area

def test_rectangle():
    assert get_area("rectangle", width=5, height=10) == 50

def test_square():
    assert get_area("square", side=4) == 16

def test_circle():
    assert get_area("circle", radius=3) == 28.26
