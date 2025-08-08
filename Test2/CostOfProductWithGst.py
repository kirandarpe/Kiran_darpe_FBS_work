#cost of products after adding gst
product1=int(input("enter the cost of product1 :"))
product2=int(input("enter the cost of product2 :"))
product3=int(input("enter the cost of product3 :"))
product4=int(input("enter the cost of product4 :"))
product5=int(input("enter the cost of product5 :"))
sum=product1+product2+product3+product4+product5
gst=sum*0.18
total_cost_of_prodct=gst+sum
print(f"cost of product after adding gst is: {total_cost_of_prodct}")