#2-5    section-2
n  = 1000

def calc(n):  
    if n == 1:
        return 1

    if n % 2:
        return 1 + calc(3 * n + 1)

    return 1 + calc(n / 2)

longest = 1
val = 1
for i in range(1, n):
    iter = calc(i)
    if longest < iter:
        val = i
        longest = iter

print('longest sequence is for number', val, 'with length', longest)