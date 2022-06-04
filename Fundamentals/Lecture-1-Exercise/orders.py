orders = int(input())
total_sum = 0

for order in range(orders):

    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())

    current_order_price = days * capsule_count * price_per_capsule
    total_sum += current_order_price
    print(f"The price for the coffee is: ${current_order_price:.2f}")


print(f"Total: ${total_sum:.2f}")