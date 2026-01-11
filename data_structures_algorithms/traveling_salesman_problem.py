def verify_tsp(paths, dist, actual_path):
    sum_dist = 0
    for i in range(1, len(actual_path)):
        sum_dist += paths[actual_path[i-1]][actual_path[i]]
    if sum_dist < dist:
        return True
    return False

def tsp(cities, paths, dist):
    cities_perm = permutations(cities)
    for perm in cities_perm:
        sum_dist = 0
        for i in range(1, len(perm)):
            sum_dist += paths[perm[i-1]][perm[i]]
        if sum_dist < dist:
            return True
    return False

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

# if __name__ == "__main__":
#     cities = [0, 1, 2, 3, 4, 5, 6, 7]
#     paths = [
#             [0, 63, 824, 940, 561, 937, 14, 95],
#             [63, 0, 736, 860, 408, 727, 844, 803],
#             [824, 736, 0, 684, 640, 1, 626, 505],
#             [940, 860, 684, 0, 847, 888, 341, 249],
#             [561, 408, 640, 847, 0, 747, 333, 720],
#             [937, 727, 1, 888, 747, 0, 891, 64],
#             [14, 844, 626, 341, 333, 891, 0, 195],
#             [95, 803, 505, 249, 720, 64, 195, 0],
#             ] 
#     dist = 1066
#     expected_output = False
#     print(tsp(cities, paths, dist))


# Traveling Salesman Problem
# A famous example of a problem in NP is the Traveling Salesman Problem, also known as TSP.

# The version of the problem that we will solve can be stated:
    # Given a list of cities, the distances between each pair of cities, and a total distance, 
    # is there a path through all the cities that is less than the distance given?