# Accept no. of passengers from user and per ticket cost.
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
num=int(input("enter the number of passenger's:"))
price_of_ticket=int(input("enter the price of ticket:"))
dis_child=price_of_ticket*0.30
dis_senior_citizen=price_of_ticket*0.50
for i in range(1,num+1):
    age=int(input("Enter the age of passenger"))
    if(age<=12):
        print("child ticket is:",price_of_ticket-dis_child)
    elif(age>=59):
        print("senior citizen ticket is:",price_of_ticket-dis_senior_citizen)
    else:
        print("price of ticket is:",price_of_ticket)
