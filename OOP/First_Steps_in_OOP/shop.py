class Shop:
    def __init__(self,name:str,items:list) -> None:
        self.name = name
        self.items = items

    def get_items_count(self):
        prod_len = len(self.items)
        return prod_len


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())