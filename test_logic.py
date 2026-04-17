from geometry import triangle_area,rectangle_area,square_area,circle_area,cylinder_surface
import pytest

def test_triangle_area():

    assert triangle_area(4,5) == 10

def test_rectangle_area():

    assert rectangle_area(2,5) == 10

def test_square_area():

    assert square_area(6) == 36
    assert square_area(5) == 25

def test_circle_area():

    assert circle_area(6) == pytest.approx(113.097, rel=1e-3)

def test_cylinder_surface():

    assert cylinder_surface(3,4) == pytest.approx(131.946, rel=1e-3)

if __name__ == "__main__":

    test_triangle_area()
    test_rectangle_area()
    test_circle_area()
    test_square_area()
    test_cylinder_surface()