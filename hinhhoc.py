import math

#Hình chữ nhật
def chu_vi_hcn(dai,rong):
    return 2* (dai+rong)

def dien_tich_hcn(dai,rong):
    return dai*rong

#Hình Tam giác
def chu_vi_tg(a,b,c):
    return a+b+c

def dien_tich_tg(a,b,c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a)(p - b)(p - c))

#Hình tròn
def chu_vi_ht(r) :
    return 2 * math.pi * r

def dien_tich_ht(r):
    return math.pi **r*2
