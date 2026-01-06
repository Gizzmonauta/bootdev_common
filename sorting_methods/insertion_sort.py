def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums


if __name__ == "__main__":
    print(f"Test case: [4, 3, 2, 1], Result: {insertion_sort([4, 3, 2, 1])}")  # Example usage
    print(f"Test case: [9, 5, -3, 7], Result: {insertion_sort([9, 5, -3, 7])}")  # Example usage
    print(f"Test case: [], Result: {insertion_sort([])}")
    print(f"Test case: [1], Result: {insertion_sort([1])}")
    print(f"Test case: [5, 3, 4, 1, 2], Result: {insertion_sort([5, 3, 4, 1, 2])}")
    print(f"Test case: [0, -2, -5, 3, 2, 1], Result: {insertion_sort([0, -2, -5, 3, 2, 1])}")
    print(f"Test case: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], Result: {insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])}")