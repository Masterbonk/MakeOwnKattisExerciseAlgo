##Sums the given array
def sum_arr(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum

##OLD
##Fins subsequences in the given array
def odl_find_subsequences(arr, s, e, counter):
    sum = sum_arr(arr[s:e])
    if (e-1 == len(arr) and len(arr[s:e]) != 1 and sum == 47):
        counter =+ 1
        find_subsequences(arr, (s+1), e, counter)
    elif (e-1 == len(arr) and len(arr[s:e]) != 1):
        find_subsequences(arr, (s+1), e, counter)
    elif (e-1 == len(arr) and len(arr[s:e]) == 1):
        return counter
    elif (len(arr[s:e]) == 1 and sum > 47):
        find_subsequences(arr, s, (e+1), counter)
    elif (sum < 47):
        find_subsequences(arr, s, (e+1), counter)
    elif (sum == 47):
        counter += 1
        find_subsequences(arr, (s+1), e, counter)
    elif (sum > 47):
        find_subsequences(arr, (s+1), e, counter)
    return counter

##NEW
#Finds subsequences
def find_subsequences(arr):
    s = 0
    e = 1
    while True:
        sum = sum_arr(arr[s:e])
        if (e-1 == len(arr) and len(arr[s:e]) != 1 and sum == 47):
            counter =+ 1
            s += 1
        elif (e-1 == len(arr) and len(arr[s:e]) != 1):
            s += 1
        elif (e-1 == len(arr) and len(arr[s:e]) == 1):
            break
        elif (len(arr[s:e]) == 1 and sum > 47):
            e += 1
        elif (sum < 47):
            e += 1
        elif (sum == 47):
            counter += 1
            s += 1
        elif (sum > 47):
            s += 1
    return counter

##----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    print(find_subsequences(lst))