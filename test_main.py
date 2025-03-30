from main import calculate_area

def test_calculate_area():
    assert calculate_area("rectangle", width=5, height=4) == 20
    assert calculate_area("circle", radius=3) == 28.274333882308138
