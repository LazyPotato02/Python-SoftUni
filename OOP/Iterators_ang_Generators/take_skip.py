class take_skip():

    def __init__(self, step, count) -> None:
        self.step = step
        self.count = count
        self.number = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            num_to_return = self.number
            self.number += self.step
            self.counter += 1
            return num_to_return
        else:
            raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)