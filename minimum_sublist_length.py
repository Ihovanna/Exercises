def minimum_sublist_length(numbers, target):

    min_length = len(numbers) + 1
    
    for i in range(0, len(numbers)):
        current_sum = numbers[i]
        ending_i = i + 1

        while ending_i < len(numbers) and current_sum + numbers[ending_i] <= target:
            current_sum += numbers[ending_i]
            ending_i += 1

        if current_sum == target and ending_i - i < min_length:
            min_length = ending_i - i

    if min_length == len(numbers) + 1:
        return None
    
    return min_length

print(minimum_sublist_length([1,2,3,4], 7))
# print(minimum_sublist_length([1,2,3,4,5], 5))
# print(minimum_sublist_length([12], 12))
# print(minimum_sublist_length([], 2))