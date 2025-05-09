##Sums up the array -   runtime: O(n)
def sum_arr(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum

##Generates all subsets
def get_subsets(arr):
    subsets = [[]] ##Necessary to keep track of the subsets
    indexes = [[]]
    interesting = [[]] ##For the ones that sum to 47
    int_index = [[]]
    for elem in arr:
        for i in range(len(subsets)):
            subset = subsets[i] + [elem]
            index = indexes[i] + [arr.index(elem)]
            subsets.append(subset)
            indexes.append(index)
            if sum_arr(subset) == 47:
                interesting.append(subset)
                int_index.append(index)
    return interesting[1:], int_index ##To remove the empty set at the start


#Testing to with recursion
def rec(arr, i, subset, subsets):
    if i == len(subsets):
        subsets.append(subset.copy())
    else:
        rec(arr, i + 1, subset+arr[i], subsets)
        rec(arr, i + 1, subsets[i], subsets)

def alt_get_subsets(arr):
    subsets = []
    subset = []
    rec(arr, 0, subset, subsets)
    return subsets




##Make function to clean up and make sure numbers don't repeat
##Cleans out sets with duplicate entries

##---------------------------------------------------------------
cases = int(input())

for i in range(cases):
    input()  #To deal with the line before each case
    amount = int(input())
    lst = input().strip().split()

    ##TESTS
    ##print(amount)
    ##print(lst)
    ##print(sum_arr(lst))
    interesting, _ = get_subsets(lst)
    print(interesting)
    print(len(interesting))

    inter = alt_get_subsets(interesting)


