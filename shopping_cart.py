#create shopping cart programme that will continue to ask for items until the user types done
foods = []
prices = []
total = 0
 
while True:
     food = input("Enter food item to buy or press  q to quit: ")
     if food.lower() == "done" or food.lower() == "q":
         break
     else:
         foods.append(food)
         price = float(input("Enter price: "))
         prices.append(price)

print("\nYour shopping cart contains:")

for food in foods:
    print(food)
    
for price in prices:
    total += price
    
print(f"\nTotal price: R{total:.2f}")