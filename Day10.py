#To find the Electricity using unit consumed
# Where If 100 units consumed=2 Ru. per unit
# for next 100 units = 3 Ru. per unit
# above 200 units=5 Ru. per unit

unit=int(input("Enter the unit consumed:"))

if unit<=100:
    bill=100*2
elif unit<=200:
    bill= 100*2+(unit-100)*3
else:
    bill=100*2+100*3+(unit-200)*5
print("The Total units consumed:",unit)
print("The Total Electricity Bill is:",bill)


