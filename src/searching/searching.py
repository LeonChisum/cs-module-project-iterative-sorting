def linear_search(arr, target):
    # Your code here
    i = 0

    while i < len(arr):
        if arr[i] == target:
            print("found")
            return i
        i = i + 1
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # setting the lowest and highest indexes of given data
    lower_idx = 0
    upper_idx = len(arr) - 1

    while lower_idx <= upper_idx:
        # dividing the 2 indexes to receive the middle index value of the data
        mid_idx = (lower_idx + upper_idx) // 2

        if arr[mid_idx] == target:
            return mid_idx
        else:
            if arr[mid_idx] < target:
                # cutting out the left side of data by setting the lower idx
                lower_idx = mid_idx
            else:
                upper_idx = mid_idx

    return -1  # not found
