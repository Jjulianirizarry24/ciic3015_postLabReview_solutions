import math

def circle_area(radius):
    return  math.pi * radius ** 2
    
def square_area(side):
    return   side ** 2
    
def triangle_area(base,height):
    return   0.5 * base * height
    
def rectangle_area(width,height):
    return  width * height
    
def calculate_area(shape):
    
    if shape == 'circle':
        radius = float(input("Radius: "))
        print("Circle area:",circle_area(radius))
    
    elif shape == 'square':
        side = float(input("Side length: "))
        print("Square area:",square_area(side))
    
    elif shape == 'triangle':
        base = float(input("Base: "))
        height = float(input("Height: "))
        print("Triangle area:",triangle_area(base,height))
    
    elif shape == 'rectangle':
        width = float(input("Width: "))
        height = float(input("Height: "))
        print(f"Rectangle area:",rectangle_area(width,height))
    
    else:
        print("Invalid shape.")


