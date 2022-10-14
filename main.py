
print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N  \n")
extra_cheese = input("Do you want extra cheese? Y or N  \n")

bill = 0
#Pizza price sizes check 👇
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
# else:
#     print("Please make sure you entered CAPS Letter")

#Adding pepperoni price 👇 
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
#extra_cheese price 👇
if extra_cheese == "Y":
  bill +=1
  
#Printing the total bill 👇
print(f"Your final bill is $ {bill}")
  
  






