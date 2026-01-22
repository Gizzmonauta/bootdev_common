"""
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of 
distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary 
that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest 
possible to please Mary and John?

Example:
With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],
[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 
corresponding towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as 
parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and 
ls (list of distances, all distances are positive or zero integers and this list has at least one 
element). The function returns the "best" sum ie the biggest possible sum of k distances less than or 
equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on 
the language. In that case with C, C++, D, Dart, Fortran, F#, Go, Julia, Kotlin, Nim, OCaml, Pascal, 
Perl, PowerShell, Reason, Rust, Scala, Shell, Swift return -1.

Examples:
ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, D, Rust, Swift, Go, ...)

ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228

Notes:
- try not to modify the input list of distances ls
- in some languages this "list" is in fact a string (see the Sample Tests).
"""

from itertools import combinations

def choose_best_sum_my_solution(t, k, ls):
    """
    It works but is less efficient and less pythonic than the refactored version below.
    """
    list_of_cities = ls.copy()
    if k > len(list_of_cities):
        return None
    
    best_sum = -1
    for combo in combinations(list_of_cities, k):
        current_sum = sum(combo)
        if best_sum < current_sum <= t:
            best_sum = current_sum
    if best_sum == -1:
        return None
    return best_sum


from itertools import combinations

def choose_best_sum(t, k, ls):
    # Efficiency Optimization: Filter out distances that are already too big.
    # Since all distances are positive, any single city > t can never be part of the sum.
    # This also effectively creates a copy, protecting the original list.
    valid_cities = [d for d in ls if d <= t]
    
    # 1. Create a generator of all possible sums (lazy evaluation)
    # 2. Filter them to keep only those <= t
    valid_sums = (sum(combo) for combo in combinations(valid_cities, k) if sum(combo) <= t)
    
    # Return the largest sum found, or None if no sums exist (e.g., if generator is empty)
    return max(valid_sums, default=None)

"""
Key Improvements
Memory Efficiency (Generators): Instead of calculating every combination and storing it in a list, 
we use a generator expression (...). This generates one sum at a time, checks it, and feeds it to 
max(), keeping memory usage near zero regardless of how large ls is.

Pythonic max(): The max() function has a built-in argument default. If the generator is empty (which 
covers your k > len edge case automatically), it returns None. This removes the need for your if 
blocks and manual flag variables (best_sum = -1).

Algorithmic Efficiency (Pre-filtering): The line valid_cities = [d for d in ls if d <= t] removes 
cities that are impossible to use before we even start generating combinations. This significantly 
reduces the work combinations has to do.

Implicit Copy: The list comprehension [d for d in ls...] creates a new list. This satisfies the "do 
not modify original input" requirement without needing an explicit .copy().
"""