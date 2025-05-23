from collections import defaultdict

#Makes a prefix sum array of the given array
def make_prefix_sum_arr(arr):
    prefix = [0]*len(arr)
    tracker = defaultdict(0)
    for i in range(len(arr)):
        if i == 0:
            tracker[(int(arr[i]))] += 1
            prefix[i] = (int(arr[i]))
        else:
            tracker[int(arr[i]) + int(prefix[i-1])] += 1
            prefix[i] = (int(arr[i]) + int(prefix[i-1]))
    return prefix, tracker

#Counts the subsequences that sum to 47
def count_subsequences(arr, tracker):
    counter = 0
    for i in range(len(arr)):
        if arr[i] + 47 in tracker:
            counter += tracker[arr[i]]
    return counter

#----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    psa, tracker = make_prefix_sum_arr(lst)
    #print(psa)
    print(count_subsequences(psa, tracker))
