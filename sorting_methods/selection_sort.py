def selection_sort(nums):
    for i in range(0, len(nums)-1):
        smallest_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums

if __name__ == "__main__":
    result = [5, 3, 8, 6, 1, 9]
    sorted_result = selection_sort(result)
    print(f"Test case: [5, 3, 8, 6, 1, 9], Result: {sorted_result}")
    result = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_result = selection_sort(result)
    print(f"Test case: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], Result: {sorted_result}")
    result = []
    sorted_result = selection_sort(result)
    print(f"Test case: [], Result: {sorted_result}")
    result = [1]
    sorted_result = selection_sort(result)
    print(f"Test case: [1], Result: {sorted_result}")
    result = [1, 2, 3, 4, 5]
    sorted_result = selection_sort(result)
    print(f"Test case: [1, 2, 3, 4, 5], Result: {sorted_result}")
    result = [15, 12, 8, 7, 5, 3, 1]
    sorted_result = selection_sort(result)
    print(f"Test case: [15, 12, 8, 7, 5, 3, 1], Result: {sorted_result}")