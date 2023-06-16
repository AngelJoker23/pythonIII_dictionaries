def calculate_square_footage(length, width):
    area = length * width
    return area

def calculate_circumference(radius):
    circumference = 2 * 3.14159 * radius
    return circumference

length = float(input("Enter the length of the house: "))
width = float(input("Enter the width of the house: "))
square_footage = calculate_square_footage(length, width)
print("The square footage of the house is:", square_footage)

radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print("The circumference of the circle is:", circumference)