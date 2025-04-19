class Counter:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += self.step
            return num
        raise StopIteration  # حلقه فور نسبت به این ارور حساس است و خودکار از حلقه خارج می‌شود # auto Break


for num in Counter(10, 20, 3): print(num)
print("------")
for num in Counter(10, 20): print(num)
