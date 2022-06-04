class Inventory:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self) -> str:
        final_capacity = self.capacity - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {final_capacity}"

inventory = Inventory(2) 
inventory.add_item("potion") 
inventory.add_item("sword") 
print(inventory.add_item("bottle")) 
print(inventory.get_capacity()) 
print(inventory) 