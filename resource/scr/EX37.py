def aligned(num):
    s = str(num)
    print("Left aligned:", s.ljust(10))
    print("Right aligned:", s.rjust(10))
    print("Center aligned:", s.center(10))


n = float(input("Enter a number: "))
aligned(n)