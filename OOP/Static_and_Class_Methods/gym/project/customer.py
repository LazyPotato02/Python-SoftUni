class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str) -> None:
        self.id = self.get_next_id()
        self.name = name
        self.address = address
        self.email = email

    @staticmethod
    def get_next_id():
        result= Customer.id
        Customer.id += 1
        return result

    def __repr__(self) -> str:
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'