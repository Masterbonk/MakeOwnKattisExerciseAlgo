
#Makes a prefix sum array of the given array
def make_prefix_sum_arr(arr):
    prefix = []
    #counter = 0
    for i in range(len(arr)):
        if i == 0:
            prefix.append(int(arr[i]))
        else:
            prefix.append(int(arr[i]) + int(prefix[i-1]))
    return prefix

#Counts the subsequences that sum to 47
def count_subsequences(prefix):
    counter = 0
    for i in range(len(prefix)):
        if prefix[i] == 47:
            counter += 1 ##This runs
        for j in range(i+1,len(prefix)):
            if (prefix[j] - prefix[i]) == 47:
                #print(str(i))
                counter += 1
    return counter

#----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    prefix = make_prefix_sum_arr(lst)
    #print(psa)
    print(count_subsequences(prefix))
