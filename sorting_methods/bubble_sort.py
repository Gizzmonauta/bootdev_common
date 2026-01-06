from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    swapping: bool = True
    end: int = len(nums)
    ordered_nums: List[int] = nums.copy()
    while swapping:
        swapping = False
        for i in range(1, end):
            if ordered_nums[i-1] > ordered_nums[i]:
                t = ordered_nums[i-1]
                ordered_nums[i-1] = ordered_nums[i]
                ordered_nums[i] = t
                swapping = True
        end -= 1
    return ordered_nums

if __name__ == "__main__":
    # Example usage
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted list:", sample_list)
    sorted_list = bubble_sort(sample_list)
    print("Sorted list:", sorted_list)