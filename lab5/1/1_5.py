# Cost Minimization

# parameters
Inf = 1000000

# variables
C = 50
F = 0.1
N = 5
D = [0, 300,450,700,900,1100,1200]
P = [0, 1100,1500,900,2100,1300]

maxDist = C / F
def min_cost(idx):
    if (D[-1] - D[idx]) > maxDist:
        minCost = min_cost(idx + 1) + P[idx]
        for i in range(idx + 2, N + 1):
            if (D[i] - D[idx]) <= maxDist:
                cost = min_cost(i) + P[idx]
                if minCost > cost:
                    minCost = cost
            else:
                break
        return minCost
    return P[idx]


cost = min_cost(0)
print(cost)