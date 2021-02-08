#!/usr/bin/env python
# coding: utf-8
# Lilly Fiorino created Feb 07, 2021

import math

def mag(v) :
    radand = 0
    for x in v :
        radand += x * x
    return math.sqrt(radand)

def unitV(v) :
    f = []
    m = mag(v)
    for x in v :
        f.append(x / m)
    return f

def dotP(v, u) :
    sum = 0
    for x in range(0,  min(len(v), len(u))) :
        sum += v[x]*u[x]
    return sum

def angleV(v, u) :
    m = mag(v) * mag(u)
    if m == 0 : return None
    return math.acos( dotP(v, u) / m ) * (180/math.pi)


# vec1 = [2, 3]
vec2 = [7, 4, 3]
# vec3 = [0, 1]
# vec4 = [2, 0]

# print(dotP(vec1, vec2))
# print(dotP(vec3, vec4))
# print(angleV(vec1, vec2))
# print(angleV(vec3, vec4))
r = 10
for z in range(-r, r) :
    for y in range(-r, r) : 
        for x in range(-r, r) : 
            if dotP(vec2, [x, y, z]) == 0 : 
                print([x, y, z], angleV(vec2, [x, y, z]))     
    