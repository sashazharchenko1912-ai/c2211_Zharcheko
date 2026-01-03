class MyIterable:
    def __iter__(self):
        return self.generator()

    def generator(self):
        yield 1
        yield 2
        yield 3


for x in MyIterable():
    print(x)
