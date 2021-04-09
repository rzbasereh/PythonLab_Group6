#2-5

def calc(n):  
    n = int(n)
    if n == 1:
        print(n, end='.\n')
    else:
        print(n, end=', ')
        if n % 2:
            n = 3 * n + 1
        else:
            n /= 2
        calc(n)

n = int(input('Enter a number: '))
calc(n)
