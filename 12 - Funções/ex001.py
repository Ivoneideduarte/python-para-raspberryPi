def fib(nFinal):
    a = 0
    b = 1
    while a < nFinal:
        numFib = a
        print(numFib, end=' ')
        a = b
        b = numFib + a
    print('\n')
    return numFib
print(fib(1000))