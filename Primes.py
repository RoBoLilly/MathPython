#!/usr/bin/env python
# coding: utf-8


def factors(n):
    f = []
    for d in list(range(1, n+1)) :
        if not (round(n/d)-(n/d)) :
            f.append(d)
    return f

def isPrime(n):
    return len(factors(n)) == 2

def primes(n):
    f = []
    for d in list(range(1, n)) :
        if isPrime(n) :
            f.append(d)
    return f

def commonFactors(n, m):
    l = []
    for f in factors(n):
        for g in factors(m):
            if g == f:
                l.append(f)
    return l

def primeFactors(n):
    return [x for x in factors(n) if isPrime(x) ]

def commonPrimeFactors(n, m):
    l = []
    for f in primeFactors(n):
        for g in primeFactors(m):
            if g == f:
                l.append(f)
    return l

def GCD(x, y) :
    return max(commonPrimeFactors(x, y) if len(commonPrimeFactors(x, y)) != 0 else [0])

# Examples




print("GCD(2021, 4465) = ", GCD(2021, 4465))
print("GCD(9, 15) = ", GCD(9, 15))


print("factors(15)", factors(15))

print("commonFactors(512, 43) = ", commonFactors(512, 43))
            


