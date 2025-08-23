# write a program to find area of rectangle using function
# define the function
def area_of_rectangle(length,width):
    return length*width
# input from user
length=float(input("Enter the length of rectangle:"))
width=float(input("Enter the width of rectangle:"))
# call a function
area=area_of_rectangle(length,width)
print(f" area of rectangle is:{area}")