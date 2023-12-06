class Distribution_Func():
    def __init__(self, values):
        self.values = sorted(values)
        self.probabilities = [(i + 1) / len(values) for i in range(len(values))]
    def distr_val(self, t):
        for count, i in enumerate(self.values):
            if i >= t and count != 0:
                return self.probabilities[count - 1]
            if i >= t and count == 0:
                return 0
        return 1

if __name__ == '__main__':
    values = [1, 2, 3]
    a = Distribution_Func(values)
    print(a.probabilities)
    print(a.values)
    print(a.distr_val(3.0001))