Year=int(input("Enter the year:"))
if( Year%4==0):
    if(Year%100==0):
        if(year%400==0):
            print("year is leaf year")
        else:
            print("year is not leaf year")
    else:
        print("year is leaf year")
else:
    print("year is not leaf year")