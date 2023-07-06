def max_contiguous_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_so_far = float('-inf')
    current_sum = 0

    size = len(arr)

    for i in range(0, size):
        current_sum = current_sum + arr[i]
        if max_so_far < current_sum:
            max_so_far = current_sum

        if current_sum < 0:
            current_sum = 0
    
    return max_so_far

print(max_contiguous_sum([-2,-3,4,-1,-2,1,5,-3]))