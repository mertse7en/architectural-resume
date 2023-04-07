def get_factorial(n: int):
    print(n)
    if n == 1:
        return 1
    else:
        return n * get_factorial(n-1)
    

print(get_factorial(5))
# 5 * get_factorial(4)  --- 4 * get_factorial(3) --- 3 * get_factiroal(2) --- 2 * get_factorial(1)