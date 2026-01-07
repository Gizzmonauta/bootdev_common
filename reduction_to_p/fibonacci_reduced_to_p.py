def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    grandparent = 0
    parent = 1
    for i in range(n-1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current

def main():
    print(f"Input : 1, Espected: 1 \nActual: {fib(1)}\n")
    print(f"Input : 10, Espected: 55 \nActual: {fib(10)}\n")
    print(f"Input : 20, Espected: 6765 \nActual: {fib(20)}\n")
    print(f"Input : 0, Espected: 0 \nActual: {fib(0)}\n")
    print(f"Input : 40, Espected: 102334155 \nActual: {fib(40)}\n")
    print(f"Input : 70, Espected: 190392490709135 \nActual: {fib(70)}\n")
    print(f"Input : 160, Espected: 1226132595394188293000174702095995 \nActual: {fib(160)}\n")

if __name__ == "__main__":
    main()


# This is an inefficient recursive version for reference
# It is exponentially slow for large n. it has a Big O(2^n) time complexity.
# Fib(40) takes about a few seconds, Fib(50) takes about a minute, Fib(70) takes about 20 hours.
#  
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
    