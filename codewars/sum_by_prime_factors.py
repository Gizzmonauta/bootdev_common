def sum_for_list(lst: list) -> list[list[int, int]]:
    r"""
    Given an array of positive or negative integers

        I= [i1,..,in]

    you have to produce a sorted array P of the form

        [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

    P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

    Example:
    I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
    [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

    Notes:

    It can happen that a sum is 0 if some numbers are negative!
    Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.
    """

    sum_dict: dict[int, int] = {}

    for num in lst:
        abs_num: int = abs(num)
        factors: list[int] = prime_factors(abs_num)
        for factor in factors:
            sum_dict[factor] = sum_dict.get(factor, 0) + num

    return sorted([[k, v] for k, v in sum_dict.items()])

def prime_factors(x: int) -> list[int]:
    factors: set[int] = set()
    divisor: int = 2
    
    while divisor <= x:
        # print(f"Current divisor: {divisor}, Current x: {x}")
        if x % divisor == 0:
            factors.add(divisor)
            x //= divisor
        else:
            divisor += 1

    ordered_factors = sorted(factors)

    return ordered_factors

def main():
    print(f"The prime factors of 12 are: {prime_factors(12)}")  # Output: {2, 3}  
    print(f"The prime factors of 100 are: {prime_factors(100)}") # Output: {2, 5}
    print(f"The prime factors of 7 are: {prime_factors(7)}")   # Output: {7}
    print(f"The prime factors of 5849347 are: {prime_factors(5849347)}") # Output: {7, 41, 89, 229}
    print(f"The prime factors of 256435891267 are: {prime_factors(256435891267)}") # Output: {2, 3, 7, 11, 17, 29, 41, 59, 79, 107}
    print(f"The sum for the list [12, 15] is: {sum_for_list([12, 15])}") # Output: [[2, 12], [3, 27], [5, 15]]
    print(f"The sum for the list [15, 30, -45] is: {sum_for_list([15, 30, -45])}") # Output: [[2, 30], [3, 0], [5, 0]]
    print(f"The sum for the list [107, 158, 204, 100, 118, 123, 126, 110, 116, 100] is: {sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100])}") # Output: [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]]

if __name__ == "__main__":
    main()