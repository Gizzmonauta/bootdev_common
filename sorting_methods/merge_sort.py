def merge_sort(nums):
    if len(nums) < 2:
        return nums
    sorted_left_side = merge_sort(nums[:len(nums) // 2])
    sorted_right_side = merge_sort(nums[len(nums) // 2:])
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    final += first[i:]
    final += second[j:]
    return final

if __name__ == "__main__":
    # Example usage
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted list:", sample_list)
    sorted_list = merge_sort(sample_list)
    print("Sorted list:", sorted_list)