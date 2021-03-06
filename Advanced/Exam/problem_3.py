def shopping_cart(*args):
    ll = list(args)
    meal_type = {
        'Soup': [],
        'Pizza': [],
        'Dessert': [],
    }
    max_products = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }
    for i in range(len(ll)):
        values = ll[i]
        if values == 'Stop':
            break
        p_type, product = values

        val_len = len(meal_type[p_type])
        if max_products[p_type] == val_len:
            continue

        if product not in meal_type[p_type]:
            meal_type[p_type].append(product)


    cart = meal_type
    result = ''
    sorted_collections_and_objects = ''
    for v in cart.values():

        if v:
            sorted_collections_and_objects = sorted(
                cart.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in sorted_collections_and_objects:
        type_object = tuple_[0]
        list_of_objects = tuple_[1]
        sorted_list_of_objects = sorted(list_of_objects)
        result += f"{type_object}:\n"
        for obj in sorted_list_of_objects:
            result += f" - {obj}\n"
    if not result:
        return 'No products in the cart!'
    return result.strip()


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))


# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))