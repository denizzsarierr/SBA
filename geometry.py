# Step 9. Conflict

import math
def triangle_area(base, height):
    """Calculates the area of a triangle."""
    return 0.5 * base * height
def square_area(side):
    """Calculates the area of a square."""
    return side ** 2
def circle_area(radius):
    """Calculates the area of a circle.””"""
    return math.pi * (radius ** 2)

def rectangle_area(length, width):
    """Calculates the area of a rectangle.
    This PR adds the rectangle area calculation logic.
    Closes #2 

    """
    return length * width

if __name__ == "__main__":
    # Demonstration of current logic
    print(f"Triangle Area (b=10, h=5): {triangle_area(10, 5)}")
    print(f"Square Area (a=4): {square_area(4)}")


