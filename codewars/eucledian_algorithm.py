def solution(lst):
    if not lst:
        return 0

    current_gcd = lst[0]
    for i in range(1,len(lst)):
        a = current_gcd
        b = lst[i]
        while a != 0 and b != 0:
            # If a < b, the first modulo swaps them automatically.
            remainder = b % a
            a, b = remainder, a
        current_gcd = b
    return current_gcd * len(lst)

def pythonic_solution(lst):
    # Handle empty lists or None
    if not lst:
        return 0
        
    current_gcd = lst[0]
    
    for i in range(1, len(lst)):
        a = current_gcd
        b = lst[i]
        
        # Euclidean Algorithm
        while b != 0:
            # We use b as the divisor. 
            # If a < b, the first modulo swaps them automatically.
            a, b = b, a % b
            
        current_gcd = a
        
    return current_gcd * len(lst)

def main():
    print(solution([2,4,6,8,10]))
    print(solution([6, 9, 21]))
    print(solution([1, 21, 55]))
    print(solution([13,26,39,52]))  #
    print(solution(None))           # Output: 0
    print(solution([17]))           # Output: 17

if __name__ == "__main__":
    main()