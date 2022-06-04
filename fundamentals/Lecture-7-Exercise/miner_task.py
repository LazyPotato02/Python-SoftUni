def miner_task():
    items_dict = {}


    while True:
        resources = input()


        if resources == "stop":
            break

        quantity = int(input())

        if resources not in items_dict:
            items_dict[resources] = quantity
        else:
            items_dict[resources] += quantity

    for key, value in items_dict.items():
        print(f"{key} -> {value}")

miner_task()