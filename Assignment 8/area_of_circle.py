# WAP to find area of circle

# define the function
def area_of_circle(radious):
    return 3.14*radious**2
radious=int(input("enter the radious of circle:"))
# call the function
area=area_of_circle(radious)
print(f" area os circle is:{area}")