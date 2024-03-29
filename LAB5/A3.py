def sum_list(lst):
    if not lst:
        return 0
    elif (len(lst)==1):
        return lst[0]
    else:
        return lst[0]+sum_list(lst[1:])

numbers = [1, 2, 3, 4, 5]
total_sum = sum_list(numbers)
print("The sum of the elements in the list is:", total_sum)
