import math

def chu_vi_tg(a, b, c):
    return a + b + c

def dien_tich_tg(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
