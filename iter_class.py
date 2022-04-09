class Counter:
    def __init__(self, num):
        self.num = num
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.num :
            cc = self.counter
            self.counter += 1
            print(cc)
            return cc
        raise StopIteration


c1 = Counter(5)

print(list(c1))