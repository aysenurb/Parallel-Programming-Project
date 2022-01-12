import numpy as np
import random
import time


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2-self.t1


class FindE:
    def __init__(self):
        self.e = 0
        self.ns = []

    def generate_numbers(self, iteration):
        for i in range(iteration):
            counter = 0
            n = 0
            while True:
                x = random.uniform(0, 1)
                n += x
                counter += 1
                if n > 1:
                    break
            self.ns.append(counter)

    def value_of_e(self):
        self.e = np.average(self.ns)
        return self.e
