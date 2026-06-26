# Authors: Daniel Bolivar and Jeremy Astaiza
# Solution of problem: "The Full Counting Sort" HackerRank https://www.hackerrank.com/challenges/countingsort4/problem
arr = [
    ['0','ab'],['6','cd'],['0','ef'],['6','gh'],['4','ij'],['0','ab'],['6','cd'],['0','ef'],['6','gh'],
    ['0','ij'],['4','that'],['3','be'],['0','to'],['1','be'],['5','question'],['1','or'],['2','not'],['4','is'],
    ['2','to'],['4','the']
]
arr2 = [
    ['1','e'],['2','a'],['1','b'],['3','a'],['4','f'],['1','f'],['2','a'],['1','e'],['1','b']
]

def countSort(arr):
    n = len(arr)
    half = n // 2
    
    for i in range(half):
        arr[i][1] = '-'

    max_val = 100

    order_list = []
    for x in range(max_val):
        order_list.append([])
    
    for x, s in arr:
        order_list[int(x)].append(s)

    # return 
    result = []
    for items in order_list:
        for item in items:
            result.append(item)

    return " ".join(result)


print(countSort(arr))
print(countSort(arr2))