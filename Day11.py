# To Calculate Shoping Bill where the user can do
# 1.Can add Product And quantities
# 2.Can apply for discount and get the bill for product
total=0
n=int(input("Enter the No. of product you want to buy:"))
for i in range(n):
    name=input("Enter the name of product:")
    qty=int(input("\nenter the quantity:"))
    price=float(input("Enter the price:"))
    amount=qty*price
    print("Amount for",name,"=",amount)
    total=total+amount
print("\n---------------------")
print("Total amount of purchase Amount=",total)
if total>=5000:
    discount=total*0.20
elif total>=2000:
    discount=total*0.10
elif total>=1000:
    discount=total*0.05
else:
    discount=0
final_total=total-discount
print("The discount for you:",discount)
print("The total bill after applying discount is:",final_total)    
