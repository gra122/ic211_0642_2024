#DUKA SMART BILLING SYSTEM
#customer information
customer_name=input("enter customer name:")
customer_age=int(input("enter customer age:"))
print("\nwelcome to duka smart,",customer_name + "!", "(age:", customer_age,")")
# collect 3 items
#item 1
item1_name = input("\n enter name of item1:")
item1_quantity=int(input("enter quantity of item 1:"))
item1_price = float(input("enter price per unit of item 1:"))
item1_total=item1_quantity*item1_price
#item 2
item2_name=input("\n enter name of item 2:")
item2_quantity=int(input("enter the quantity of item 2:"))
item2_price = float(input("enter price per unit of item 2:"))
item2_total=item2_quantity*item2_price
#item3
item3_name = input("\n enter name of item3:")
item3_quantity=int(input("enter quantity of item 3:"))
item3_price = float(input("enter price per unit of item 3:"))
item3_total=item3_quantity*item3_price
#calculations
subtotal= item1_total + item2_total + item3_total
vat = subtotal * 0.16
grand_total = subtotal + vat
# cash payment and change
cash_paid = float(input("\n enter cash paid by customer:"))
change = cash_paid- grand_total
#print receipt
print("\n")
print("========= DUKA SMART RECEIPT========")
print("\n customer:", customer_name)
print("1.", item1_name,
      "x", item1_quantity,
      "= kes", format(item1_total, ".2f"))
print("2.", item2_name,
      "x", item2_quantity,
      "= kes", format(item2_total, ".2f"))
print("3.", item3_name,
      "x", item3_quantity,
      "= kes", format(item3_total, ".2f"))
print("\n-------------------------")
print("subtotal  : kes", 
     format(subtotal, ".2f") )
print("vat (16%) : kes ", format(vat, ".2f"))
print("grand_total  : kes ",
      format(grand_total, ".2f"))
print("\n cash paid  : kes ", 
      format(cash_paid, ".2f"))
#check if customer have enough money
if cash_paid>= grand_total:
    print("change   : kes", 
          format(change,  ".2f"))
else:
    shortfall=grand_total-cash_paid
    print("shortfall    : kes " ,
          format(change,  ".2f"))
print("customer needs more money.")
print("\n========thank you========")