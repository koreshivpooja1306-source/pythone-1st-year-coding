# To Find Restaurant bill Using Menu And Price
menu={
    "1":{"item":"burger","price":50},
    "2":{"item":"pizza","price":50},
    "3":{"item":"pani-puri","price":30}
}
print("-----WELCOME TO OUR RESTURANT-----")
for key,value in menu.items():
    print(f"[{key}]{value['item']}:{value['price']}")

choice=int(input("Enter your choice according to the menu:"))

if choice==1:
    qty=int(input("Enter the Quantity of your order:"))
    print("your order is burger and price is:",qty*50)

elif choice==2:
    qty=int(input("Enter the Quantity of your order:"))
    print("your order is pizza and price is:",qty*50)

elif choice==3:
    qty=int(input("Enter the Quantity of your order:"))
    print("Your order is pani-puri and price is:",30*qty)
    
else:
    print("Enter Valid Choice,Try again.")


