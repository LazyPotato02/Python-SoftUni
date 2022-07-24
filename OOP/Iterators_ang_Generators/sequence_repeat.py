class sequence_repeat():
    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.idx = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration
        if self.idx >= len(self.sequence):
            self.idx = 0
        result = self.sequence[self.idx]
        self.idx += 1
        self.counter += 1
        return result

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')