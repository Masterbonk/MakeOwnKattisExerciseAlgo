#Binary search tree
def search(arr, goal):
    counter = 0
    if arr[round(len(arr)/2)] < goal:
        search(arr[:len(arr)/2])
    elif arr[round(len(arr)/2)] > goal:
        search(arr[len(arr)/2:])
    elif arr[round(len(arr)/2)] == goal:
        #Make a function that goes backwards until it comes across something that is not goal
        counter += 1
    return counter

#----------------------------------------------

#Makes a prefix sum array of the given array
def make_prefix_sum_arr(arr):
    prefix = []
    counter = 0
    for i in range(len(arr)):
        if i == 0:
            if arr[i] == 47:
                counter += 1
            prefix.append(int(arr[i]))
        else:
            if arr[i] == 47:
                counter += 1
            prefix.append(int(arr[i]) + int(prefix[i-1]))
    return prefix, counter

#Counts the subsequences that sum to 47
# def count_subsequences(arr):
#     counter = 0
#     for i in range(len(arr)):
#         if arr[i] == 47:
#             counter += 1
#         for j in range(i+1,len(arr)):
#             if (arr[j] - arr[i]) == 47:
#                 counter += 1
#     return counter

def count_subsequences(order, arr):
    counter = 0
    for i in order:
        c = search(arr[:i], i+47)
        if c > 0:
            counter += c
        else:
            continue
    return counter

#----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    psa, counter = make_prefix_sum_arr(lst)
    sort = sorted(psa)
    #print(psa)
    print(count_subsequences(psa, sort) + counter)
