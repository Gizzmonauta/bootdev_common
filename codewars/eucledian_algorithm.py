"""
Find the greatest common divisor (GCD) of a list of integers using the Euclidean algorithm.
Return the GCD multiplied by the number of integers in the list.
If the list is empty or None, return 0.

The GCD of two integers a and b is the largest integer that divides both a and b without 
leaving a remainder.

Example:
- For the list [6, 9, 21], the GCD is 3. Since there are 3 integers in the list, the result
is 3 * 3 = 9.

The Euxledian Algorithm

(1) Begin with a given pair (a,b) where a <= b. If a < b by doing a % b the modulo operator
swaps them automátically.

(2) If the two entries of my pair (a,b) are both non-zero:
    (a) find the remainder of the division by r = a % b
    (b) Replace (a, b) with (r, a) (Note: r < a)
    (c) Return to (2)

(3) If not: the non-zero entry of the pair is the gcd

(4) Multiply the gcd by the number of items in the list.
"""

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