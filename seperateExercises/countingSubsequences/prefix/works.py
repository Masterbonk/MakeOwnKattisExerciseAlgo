
#Makes a prefix sum array of the given array
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

#Counts the subsequences that sum to 47
def count_subsequences(arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i] == 47:
            counter += 1
        for j in range(i+1,len(arr)):
            if (arr[j] - arr[i]) == 47:
                counter += 1
    return counter

#----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    psa = make_prefix_sum_arr(lst)
    #print(psa)
    print(count_subsequences(psa))
