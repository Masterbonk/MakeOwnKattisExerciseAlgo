import sys

sys.setrecursionlimit(10**6)

def find_occurrences(arr, goal, index):
    counter = 0
    i = 0
    while i == 0:
        if arr[index] == goal:
            index -= 1
        elif arr[index] < goal:
            i += 1
    while i == 1:
        if len(arr)-1 == index and arr[index] == goal:
            counter += 1
            return counter
        elif len(arr)-1 == index:
            return counter
        elif arr[index] < goal:
            index += 1
        elif arr[index] == goal:
            counter += 1
            index += 1
        elif arr[index] > goal:
            i += 1
        else:
            return counter
    return counter

#Binary search tree
def search(arr, goal):
    counter = 0
    index = round(len(arr)/2)
    if len(arr) <= 1 and arr[index] != goal:
        return counter
    elif arr[index] < goal:
        return search(arr[index:], goal)
    elif arr[index] > goal:
        return search(arr[:index], goal)
    elif arr[index] == goal:
        #Make a function that goes backwards until it comes across something that is not goal
        #c = find_occurrences(arr, goal, index)
        counter += 1 #c
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


def count_subsequences(order, arr):
    counter = 0
    for i in range(len(order)):
        c = search(arr[i:], order[i]+47)
        counter += c
    return counter

#----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    psa, counter = make_prefix_sum_arr(lst)
    sort = sorted(psa)
    print(count_subsequences(psa, sort) + counter)
