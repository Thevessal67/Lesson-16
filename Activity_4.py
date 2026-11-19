length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
def area(length, width):
    return length * width
def perimeter(length, width):
    return 2 * (length + width)

print("The area of the rectangle is: ", area(length, width))
print("The perimeter of the rectangle is: ", perimeter(length, width))
