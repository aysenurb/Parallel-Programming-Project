from classes import TicToc, FindE

if __name__ == '__main__':
    tt = TicToc()
    tt.tic()
    instance = FindE()
    instance.generate_numbers(40000000)
    result = instance.value_of_e()
    print("Value of e: %.6f" % result)
    print("Time = %.5f seconds" % tt.toc())
