def fact(n, current=1, factorial=1):
    if current > n:
        return factorial
    return fact(n, current + 1, factorial * current)

print(fact(5))  

