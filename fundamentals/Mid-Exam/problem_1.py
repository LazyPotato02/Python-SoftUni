city_count = int(input())
total_profit = 0
city_counter = 1
for i in range(city_count):
    city_name = input()
    owner_earned = float(input())
    owner_expenses = float(input())

    if city_counter % 5 == 0:
        owner_earned *= 0.9
    elif city_counter % 3 == 0:
        owner_expenses = owner_expenses + (owner_expenses * 0.5)


    city_profit = owner_earned - owner_expenses
    total_profit += city_profit
    print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")

    city_counter += 1

print(f"Burger Bus total profit: {total_profit:.2f} leva.")