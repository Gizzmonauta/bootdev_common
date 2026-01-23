r"""
How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples
Basic
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42

Explosive
exp_sum(50) # 204226
exp_sum(80) # 15796476
exp_sum(100) # 190569292
"""

def exp_sum(n):
    # Create a list to store the number of ways to form each sum up to n
    partitions = [0] * (n + 1)
    partitions[0] = 1  # There's one way to make the sum 0 (using no numbers)

    # Iterate through all integers from 1 to n
    for i in range(1, n + 1):
        # Update the partitions list for all sums that can include the integer i
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]

r"""
############# THE SOLUTION ##############

The Goal: Find the total number of ways to build a tower of Height 5.
The Rules: We introduce brick sizes one by one (Size 1, then Size 2, etc.).

Initialization: The Blank Book
Before we pick up any bricks, we set up our book.
    - Page 0 (Height 0): 1 Way (The empty floor. This is our "seed").
    - Pages 1–5: 0 Ways (We haven't started building yet).

Height  0  1  2  3  4  5
Ways    1  0  0  0  0  0
-----------------------------------------
Iteration 1: Using "Size 1" Bricks
We are now allowed to use Size 1 bricks.

1. Build Height 1:
    - Use a "1". Remainder needed: 0.
    - Check Page 0: It says 1 way.
    - Add to Page 1: 0 (current) + 1 = 1.
2. Build Height 2:
    - Use a "1". Remainder needed: 1.
    - Check Page 1: It says 1 way.
    - Add to Page 2: 0 (current) + 1 = 1.
3. Build Height 3:
    - Use a "1". Remainder needed: 2.
    - Check Page 2: It says 1 way.
    - Add to Page 3: 0 (current) + 1 = 1.
4. Build Height 4:
    - Use a "1". Remainder needed: 3.
    - Check Page 3: It says 1 way.
    - Add to Page 4: 0 (current) + 1 = 1.
5. Build Height 5:
    - Use a "1". Remainder needed: 4.
    - Check Page 4: It says 1 way.
    - Add to Page 5: 0 (current) + 1 = 1.
    
Book Status after Iteration 1:

Height | 0 | 1 | 2 | 3 | 4 | 5 |
Ways   | 1 | 1 | 1 | 1 | 1 | 1 |
-----------------------------------------
Iteration 2: Using "Size 2" Bricks
We now unlock Size 2 bricks. We start at Height 2 
(because a Size 2 brick is too big for Height 1).

1. Build Height 2:
    - Use a "2". Remainder needed: 0.
    - Check Page 0: It says 1 way.
    - Add to Page 2: 1 (current) + 1 = 2.
2. Build Height 3:
    - Use a "2". Remainder needed: 1.
    - Check Page 1: It says 1 way.
    - Add to Page 3: 1 (current) + 1 = 2
3. Build Height 4:
    - Use a "2". Remainder needed: 2.
    - Check Page 2: STOP. Look at the current book. Page 2 was updated in step 1. 
      It now says 2 ways.
    - Add to Page 4: 1 (current) + 2 = 3.
4. Build Height 5:
    - Use a "2". Remainder needed: 3.
    - Check Page 3: STOP. Look at the current book. Page 3 was updated in step 2. 
      It now says 2 ways.
    - Add to Page 5: 1 (current) + 2 = 3.

Book Status after Iteration 2:

Height | 0 | 1 | 2 | 3 | 4 | 5 |
Ways   | 1 | 1 | 2 | 2 | 3 | 3 |
-----------------------------------------
Iteration 3: Using "Size 3" Bricks
We unlock Size 3 bricks. Start at Height 3.

1. Build Height 3:
    - Use a "3". Remainder needed: 0.
    - Check Page 0: It says 1 way.
    - Add to Page 3: 2 (current) + 1 = 3.
2. Build Height 4:
    - Use a "3". Remainder needed: 1.
    - Check Page 1: It says 1 way.
    - Add to Page 4: 3 (current) + 1 = 4.
3. Build Height 5:
    - Use a "3". Remainder needed: 2.
    - Check Page 2: It says 2 ways. (It hasn't changed in this iteration).
    - Add to Page 5: 3 (current) + 2 = 5.

Book Status after Iteration 3:

Height | 0 | 1 | 2 | 3 | 4 | 5 |
Ways   | 1 | 1 | 2 | 3 | 4 | 5 |
-----------------------------------------
Iteration 4: Using "Size 4" Bricks
We unlock Size 4 bricks. Start at Height 4.

1. Build Height 4:
    - Use a "4". Remainder needed: 0.
    - Check Page 0: It says 1 way.
    - Add to Page 4: 4 (current) + 1 = 5.
2. Build Height 5:
    - Use a "4". Remainder needed: 1.
    - Check Page 1: It says 1 way.
    - Add to Page 5: 5 (current) + 1 = 6.

Book Status after Iteration 4:

Height | 0 | 1 | 2 | 3 | 4 | 5 |
Ways   | 1 | 1 | 2 | 3 | 5 | 6 |
-----------------------------------------
Iteration 5: Using "Size 5" Bricks
We unlock Size 5 bricks. Start at Height 5.

1. Build Height 5:
    - Use a "5". Remainder needed: 0.
    - Check Page 0: It says 1 way.
    - Add to Page 5: 6 (current) + 1 = 7.
    
FINAL Book Status:

Height | 0 | 1 | 2 | 3 | 4 | 5 |
Ways   | 1 | 1 | 2 | 3 | 5 | 7 |

The Result: Look at Page 5. There are 7 ways to partition the number 5.
"""