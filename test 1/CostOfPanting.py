area_of_perwall=float(input("Enter the area of perwall:"))
interiour_cost_price=float(input("enter the interiour cost pricr:"))
exteriour_cost_price=float(input("enter the exteriour cost price"))

interiour_wall=7
exteriour_wall=6
total_interiour_wall_cost=interiour_wall*interiour_cost_price*area_of_perwall
total_exteriour_wall_cost=exteriour_wall*exteriour_cost_price*area_of_perwall
total_cost_of_panting=total_exteriour_wall_cost+total_interiour_wall_cost
print(f"interiour cost price of wall is:{total_interiour_wall_cost}")
print(f"exteriour cost price of wall is :{total_exteriour_wall_cost}")
print(f"total cost price of panting is :{total_cost_of_panting}")