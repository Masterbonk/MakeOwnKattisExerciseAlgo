import sys

sys.setrecursionlimit(10**6) #This is to deal with the recursionerror. The normal limit is too small to deal with our input size


##Sums the given array
def sum_arr(arr, start,end):
    if start != 0:
        sum = arr[end]-arr[start-1]
    else:
        sum = arr[end]
    return sum

##OLD
##Fins subsequences in the given array
def find_subsequences(arr, s, e, counter, end):
    sum = sum_arr(arr[s:e])
    if (e-1 == len(arr) and len(arr[s:e]) != 1 and sum == 47):
        counter =+ 1
        find_subsequences(arr, (s+1), e, counter, end)

    elif (e-1 == len(arr) and len(arr[s:e]) != 1):
        find_subsequences(arr, (s+1), e, counter, end)

    elif (e-1 == len(arr) and len(arr[s:e]) == 1):
        return counter

    elif (len(arr[s:e]) == 1 and sum > 47):
        find_subsequences(arr, s, (e+1), counter, end)

    elif (sum < 47):
        find_subsequences(arr, s, (e+1), counter, end)

    elif (sum == 47):
        counter += 1
        find_subsequences(arr, (s+1), e, counter, end)

    elif (sum > 47):
        find_subsequences(arr, (s+1), e, counter, end)

    return counter

##NEW
#Finds subsequences
def new_find_subsequences(arr):
    s = 0
    e = 1
    counter = 0
    while True:
        sum = sum_arr(arr,s,e)
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

def make_prefix_sum_arr(arr):
    prefix = []
    #counter = 0
    for i in range(len(arr)):
        if i == 0:
            #if arr[i] == 47:
            #    counter += 1
            prefix.append(int(arr[i]))
        else:
            #if arr[i] == 47:
            #    counter += 1
            prefix.append(int(arr[i]) + int(prefix[i-1]))
    return prefix#, counter
##----------------------------------------------------------------
cases = int(input())



for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    newLst = make_prefix_sum_arr(lst)
    #print(find_subsequences(lst, 0, 1, 0, amount))
    print(new_find_subsequences(newLst))
