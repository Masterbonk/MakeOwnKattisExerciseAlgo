import sys

sys.setrecursionlimit(10**6) #This is to deal with the recursionerror. The normal limit is too small to deal with our input size

'''
Questions:
Can a subsequence overlap? Like if we have 20 27 20, can we have 20 27 and 27 20?

Does the solution not involve making an array of sums, where each new index contains the sum of itself and every element below? This way to find the sum of a sequence, we would only have to make tree operations, like so.
Say we have an array [0;1;2;3;4;5;6,7;8;9], we want a sum array, so we now have [0;1;3;6;10;15;21,28;36;45]

We want the sum of elements from index 5 to 9, we we can now do is take index 4 (10) and index 9 (45) and find the sum by taking 45-10=35. The result is found by making 3 small checks, instead of going through 5 elements, this difference will only grow bigger. Think it might be faster than current method, since it seems the sum is found for every sequence.

'''

##Sums the given array
def sum_arr(arr):
    sum = 0
    for i in arr:
        sum += int(i)
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
    s = 0 ## start
    e = 1 ## end
    counter = 0
    while True:
        sum = sum_arr(arr[s:e]) ## what if there is only 1 element in array? what if index 0 is 47?
        if (e-1 == len(arr) and len(arr[s:e]) != 1 and sum == 47): ## MAKE len(arr[s:e]) != 1 TO s != e, length might be more expensive
            ## If end is at the end of array AND start is not at end AND sum is 47
            counter =+ 1
            s += 1
        elif (e-1 == len(arr) and len(arr[s:e]) != 1): ## MAKE len(arr[s:e]) != 1 TO s != e
            ## If end is at the end of array AND start is not at end
            s += 1
        elif (e-1 == len(arr) and len(arr[s:e]) == 1): ## MAKE e-1 == len(arr) and len(arr[s:e]) == 1 TO s-1 == len(arr)
            ## If end is at the end of array AND start is at end
            break
        elif (len(arr[s:e]) == 1 and sum > 47):
            ## start is at end AND sum is above 47
            e += 1
            ## Increases end

        elif (sum < 47):
            ## sum is below 47
            e += 1
            ## Increases end

        elif (sum == 47):
            ## sum is 47
            counter += 1
            s += 1
            ## Increases start and makes the final counter go up

        elif (sum > 47):
            ## sum is above 47
            s += 1
            ## Increases end

    return counter

##----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    print(find_subsequences(lst, 0, 1, 0, amount))
    #print(new_find_subsequences(lst))