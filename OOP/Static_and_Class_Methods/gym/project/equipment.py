class Equipment:
    id = 1

    def __init__(self, name) -> None:
        self.id = self.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        result= Equipment.id
        Equipment.id += 1
        return result

    def __repr__(self) -> str:
        return f'Equipment <{self.id}> {self.name}'