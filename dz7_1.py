class IterableWithGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generator()

    def generator(self):
        current = self.start
        while current <= self.end:
            yield current
            current += 1


if __name__ == "__main__":
    numbers = IterableWithGenerator(1, 5)

    for num in numbers:
        print(num)
