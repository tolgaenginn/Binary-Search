def bin_search(nums, target):
    nums_visited = []
    low, high = 0, len(nums)-1
    while low <= high:
        mid_index = (low + high) // 2
        curr = nums[mid_index]
        nums_visited.append(curr)
        if curr == target:
            return True, nums_visited
        elif curr < target:
            low = mid_index + 1
        else:
            high = mid_index - 1
    return False, nums_visited


if __name__ == '__main__':
    example_list = [1,3,5,6,7,11,13,19,28,55,98,100]
    print(bin_search(example_list, 28))
    print(bin_search(example_list, 13))
    print(bin_search(example_list,98))
    print(bin_search(example_list,17))




