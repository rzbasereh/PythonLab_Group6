# 2-2
def gcd_calc(x, y):
    if y == 0:
        return x
    else:
        return gcd_calc(y, x % y)

x =int (input ("Enter the first number: "))   
y =int (input ("Enter the second number: "))

print(gcd_calc(x, y))
