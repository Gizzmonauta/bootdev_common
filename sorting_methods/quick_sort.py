def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle-1)
        quick_sort(nums, middle+1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low-1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1

if __name__ == "__main__":
    result = [2, 1, 3]
    quick_sort(result, 0, 2)
    print(f"Test case: [2, 1, 3], Result: {result}")
    result = [9, 6, 2, 1, 8, 7]
    quick_sort(result, 0, 5)
    print(f"Test case: [9, 6, 2, 1, 8, 7], Result: {result}")
    result = []
    quick_sort(result, 0, -1)
    print(f"Test case: [], Result: {result}")
    result = [1]
    quick_sort(result, 0, 0)
    print(f"Test case: [1], Result: {result}")
    result = [1, 2, 3, 4, 5]
    quick_sort(result, 0, 4)
    print(f"Test case: [1, 2, 3, 4, 5], Result: {result}")
    result = [5, 4, 3, 2, 1]
    quick_sort(result, 0, 4)
    print(f"Test case: [5, 4, 3, 2, 1], Result: {result}")
    result = [0, 1, 6, 4, 7, 3, 2, 8, 5, -9]
    quick_sort(result, 0, 9)
    print(f"Test case: [0, 1, 6, 4, 7, 3, 2, 8, 5, -9], Result: {result}")