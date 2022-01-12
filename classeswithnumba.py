import numpy as np
import random
import time
from numba import jit


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
        self.ns = self.generate_numbers_static(iteration)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def generate_numbers_static(iteration):
        ns = []
        for i in range(iteration):
            counter = 0
            n = 0
            while True:
                x = random.uniform(0, 1)
                n += x
                counter += 1
                if n > 1:
                    break
            ns.append(counter)
        return ns

    def value_of_e(self):
        self.e = np.average(self.ns)
        return self.e
