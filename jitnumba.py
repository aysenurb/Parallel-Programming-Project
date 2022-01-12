import numpy as np

from classeswithnumba import TicToc, FindE
from threading import Thread
import os

if __name__ == '__main__':
    tt = TicToc()
    tt.tic()

    n = 10000000
    threads = []
    instances = []
    for i in range(os.cpu_count()):
        instances.append(FindE())
        threads.append(Thread(target=instances[i].generate_numbers, args=(n,)))
        print("started thread number %d" % i)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    all_ns = []
    for instance in instances:
        all_ns.append(instance.ns)
    value_of_e = np.average(all_ns)

    print("Value of e: %.8f , Time = %.5f seconds" % (value_of_e, tt.toc()))
