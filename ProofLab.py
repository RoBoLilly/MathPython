#!/usr/bin/env python
# Lilly Fiorino created Feb 08, 2021

def factors(n) :
    f = []
    for d in list(range(1, n+1)) :
        if not n % d : # because duh
            f.append(d)
    return f

def factorial(n) :
    if n == 1 :
        # print(n)
        return 1
    else :
        # print(str(n) + "*",end='')
        return n * factorial(n - 1)

print(factorial(4))
print(factors(24))