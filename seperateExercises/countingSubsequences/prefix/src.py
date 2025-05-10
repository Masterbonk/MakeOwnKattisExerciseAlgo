import sys

sys.setrecursionlimit(10**6) #This is to deal with the recursionerror. The normal limit is too small to deal with our input size

# ##Sums the given array
# def sum_arr(arr):
#     sum = 0
#     for i in arr:
#         sum += int(i)
#     return sum

#Makes a prefix sum array of the given array
def prefix_sum_arr(arr):
    prefix = []
    for i in range(len(arr)):
        if i == 0:
            prefix.append(int(arr[i]))
        else:
            prefix.append(int(arr[i]) + int(prefix[i-1]))
    return prefix

##----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    print(prefix_sum_arr(lst))
    #print(find_subsequences(lst, 0, 1, 0, amount))
    #print(new_find_subsequences(lst))
