def reverse_list(lst):
    n=len(lst)
    for i in range (n//2):
        temp=lst[i]
        lst[i]=lst[n-i-1]
        lst[n-i-1]=temp
    return lst

original_list = [1, 2, 3, 9, 5]
reversed_list = reverse_list(original_list)

print("Reversed list:", reversed_list)
