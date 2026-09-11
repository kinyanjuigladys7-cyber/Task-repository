cow=int(input("Enter the number of cows:"))
milk_per_cow=float(input("Enter the amount of milk produced per cow (in liters):"))
milk_per_litre=float(input("Enter the price of milk per liter:"))
total_milk=cow*milk_per_cow
total_cost=total_milk*milk_per_litre
print("Total milk produced:", total_milk, "liters")
print("Total cost:", total_cost, "currency")
print("Amount of milk produced per day:", total_cost, "currency")

