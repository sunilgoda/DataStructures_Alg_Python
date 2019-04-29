'''
Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both
arrays whose sum is equal to X.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case
contains 3 lines . The first line contains 3 space separated integers N, M, X. Then in the next two lines are space
separated values of the array A and B respectively.

Output:
For each test case in a new line print the sorted space separated values of all the pairs u,v where u belongs to array
 A and v belongs to array B, such that each pair is separated from the other by a ',' without quotes also add a space
 after the ',' . If no such pair exist print -1.

Constraints:
1 <= T <= 100
1 <= N, M, X <= 106
-106 <= A, B <= 106

Example:
Input:
2
5 5 9
1 2 4 5 7
5 6 3 4 8
2 2 3
0 2
1 3
Output:
1 8, 4 5, 5 4
0 3, 2 1
'''

def findPairs(arr1,arr2, total):
    set1 = (arr1)
    set2 = (arr2)
    pairs = []
    for i in set1:
        if total - i in set2:
            pairs.append((i, total-i))

    if len(pairs) < 1:
        print("No pairs found")
        return (-1,-1)
    else:
        return pairs


for i in range(int(input("Enter number of cases: "))):
    hint = "\nEnter array1 size ,array2 size, sum to be found: "
    crit = [int(x) for x in input(hint).split()]

    while len(crit) != 3:
        crit = [int(x) for x in input(hint).split()]

    arr1_len = crit[0]
    arr2_len = crit[1]
    total = crit[2]

    arr1 = [int(x) for x in input("\nEnter array1 elements: ").split()]
    arr2 = [int(x) for x in input("\nEnter array2 elements: ").split()]

    results = findPairs(arr1,arr2,total)
    print(results)
