#!/usr/bin/env python
# coding: utf-8

import time

def factorsSlow(n):
    f = []
    for d in list(range(1, n+1)) :
        if not (round(n/d)-(n/d)) :
            f.append(d)
    return f

def factors(n) :
    f = []
    for d in list(range(1, n+1)) :
        if not n % d : # because duh
            f.append(d)
    return f

def isPrime(n):
    return len(factors(n)) == 2

def primes(n):
    f = []
    for d in list(range(1, n)) :
        if isPrime(d) :
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

def GCD_slow(x, y) :
    return max(commonPrimeFactors(x, y) if len(commonPrimeFactors(x, y)) != 0 else [0])

def GCD(x, y) : # using Euclidean Algorithm
    for l in range(0, x):
        if (x - y) == 0 :
            return o
        o = abs(x - y)
        x = min([x, y])
        y = o

# Examples

print("factors(6) = ", factors(6))
print("factors(64) = " , factors(64))
print("factors(36) = ", factors(36))
print("factors(19) = ", factors(19))

print("isPrime(6) = ", isPrime(6))
print("isPrime(64) = " , isPrime(64))
print("isPrime(36) = ", isPrime(36))
print("isPrime(19) = ", isPrime(19))

print("commonFactors(54, 4) = ", commonFactors(54, 4))
print("commonFactors(23, 3) = ", commonFactors(23, 3))
print("commonFactors(64, 128) = ", commonFactors(64, 128))
print("commonFactors(512, 43) = ", commonFactors(512, 43))


print("Primes from 1 to (30) = ", primes(30))

print("GCD(2021, 4465) = ", GCD(2021, 4465))
print("GCD(9, 15) = ", GCD(9, 15))
print("GCD(10, 15) = ", GCD(1, 15))

print("\nSpeed Tests: \n")

timerStart = time.perf_counter()
print("GCD_slow(2021, 4465) = ", GCD_slow(2021, 4465))
timerEnd = time.perf_counter()
print(f"Time in {timerEnd - timerStart:0.7f}(s)")

timerStart = time.perf_counter()
print("GCD(2021, 4465) = ", GCD(2021, 4465))
timerEnd = time.perf_counter()
print(f"Time in {timerEnd - timerStart:0.7f}(s)")

print("\n")

timerStart = time.perf_counter()
print("GCD_slow(9, 15) = ", GCD_slow(9, 15))
timerEnd = time.perf_counter()
print(f"Time in {timerEnd - timerStart:0.7f}(s)")

timerStart = time.perf_counter()
print("GCD(9, 15) = ", GCD(9, 15))
timerEnd = time.perf_counter()
print(f"Time in {timerEnd - timerStart:0.7f}(s)")

print("\n")

timerStart = time.perf_counter()
print("GCD_slow(23423, 53456) = ", GCD_slow(23423, 53456))
timerEnd = time.perf_counter()
print(f"Time in {timerEnd - timerStart:0.7f}(s)")

timerStart = time.perf_counter()
print("GCD(23423, 53456) = ", GCD(23423, 53456))
timerEnd = time.perf_counter()
print(f"Time in {timerEnd - timerStart:0.7f}(s)")

            


