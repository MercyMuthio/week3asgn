#create a function
def calculate_discount(price, discount_percent) :
   
    if discount_percent >= 20: 
          discount_amount = (price*(discount_percent/100))
          final_price = price - discount_amount 
          return final_price
    else:
      return price
#taking inputs from user
price= float(input("Enter the original price: ") )
discount_percent = float(input("Enter the Discount percentage: "))
#calling action
final_price=calculate_discount(price, discount_percent)
#Display results
if discount_percent>=20:
   print(f"Final price after {discount_percent}% discount is : {final_price}")
else:
  print(f"No discount applied. Final price is : {final_price}")
