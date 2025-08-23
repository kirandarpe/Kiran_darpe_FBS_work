#write a program to cheak year is leap year or not
def leap(num):
        if(num%4==0):
            print(f"{num}: is leap year")
        else:
            print(f"{num}: is not leap year")
num=int(input("enter the number:"))
leap(num)