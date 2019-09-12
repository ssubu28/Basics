# Bubble Sort

"""
Bubble Sort: In each pass, the largest element finds its position in the list.
Complexity: W.C = O(n^2), B.C = O(n)

1. One ref called i

2. Other ref called j to move over the list for each i. starts at i+1

i moves only if i > j -- when we need to shift the largest element all the way to the end.
else i remains same and j is incremented
"""

alist = [54,26,93,17,77,31,44,55,20]

print alist


for i in range(len(alist)):
    for j in range(i+1, len(alist)):
        if alist[i] <= alist[j]:
            j = j + 1
        else:             # swap i and j
            alist[i],alist[j] = alist[j], alist[i]


print alist
