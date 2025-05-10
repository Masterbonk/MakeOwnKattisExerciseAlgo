##Sums the given array
def sum_arr(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum

##Fins subsequences in the given array
def find_subsequences(arr, s, e):
    counter = 0
    sum = sum_arr(arr[s:e])
    if (sum < 47):
        find_subsequences(arr, s, e+1)
    if (sum == 47):
        counter += 1
        find_subsequences(arr, s+1, e)
    if (sum > 47):
        find_subsequences(arr, s+1, e)
    return counter

##----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()