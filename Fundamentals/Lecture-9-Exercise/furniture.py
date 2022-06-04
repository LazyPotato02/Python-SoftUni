import re

def furniture():
    pattern = r'>>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)'
    spend_money = 0
    product_list = []

    while True:
        data = input()

        if data == "Purchase":
            break

        result = re.match(pattern, data)

        if result is not None:
            product = result[1]
            price = float(result[2])
            quantity = float(result[3])
            spend_money += price * quantity
            product_list.append(product)

    print("Bought furniture:")

    if spend_money > 0:
        print('\n'.join(product_list))
    print(f'Total money spend: {spend_money:.2f}')


furniture()