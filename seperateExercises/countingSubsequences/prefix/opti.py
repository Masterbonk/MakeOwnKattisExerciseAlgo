from collections import defaultdict

#Makes a prefix sum array of the given array
def make_prefix_sum_arr(arr):
    prefix = [0]*len(arr)
    tracker = defaultdict(int)
    #tracker[0] = 1

    for i in range(len(arr)):
       
        if i == 0:
            tracker[(int(arr[i]))] += 1
            prefix[i] = (int(arr[i]))
        else:
            tracker[int(arr[i]) + int(prefix[i-1])] += 1
            prefix[i] = (int(arr[i]) + int(prefix[i-1])) 
    #print(tracker)
    #print(prefix)
    #tracker[max(tracker)+47] = 1
    return prefix, tracker

#Counts the subsequences that sum to 47
def count_subsequences(prefix, tracker):
    counter = 0
    for i in range(len(prefix)):
        #print(str(i) +" is i and this is prefix "+str(prefix[i]) + " tracker "+str(prefix[i]+47)+" has: "+ str(tracker[prefix[i]+47]))
        #print("Counter Before: "+str(counter))
        if i == 0 and prefix[i] == 47:
            counter += 1
        if prefix[i] + 47 in tracker:
            counter += tracker[prefix[i]+47]#*tracker[prefix[i]]#tracker.pop(arr[i]+47)*tracker[arr[i]]
        if prefix[i] in tracker:
            tracker[prefix[i]] -= 1
        #print("Counter After: "+str(counter))
    return counter

#----------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()
    prefix, tracker = make_prefix_sum_arr(lst)
    #print(psa)
    #print(tracker)
    print(count_subsequences(prefix, tracker))
