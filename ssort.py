# Selection Sort

"""
find max value in 0 to n-1 items
swap with (n-1)th item

search 0 to n-2 and find max ELEMENT
swap with (n-2)th

use i and max to check max ...till i+1 ,len(alist)
max now has the req value.

swap with n how ? outside loop ? n-1 to 0 ? yes
0 to n, 0 to n-1, 0 to n-2
"""


alist = [54,26,93,17,77,31,44,55,20]
print alist

for i in range((len(alist)-1),0,-1):
    max = 0  # set max to 0 always

    for j in range(1,i+1): # should be till i because i keeps decreasing from n to n-1 and so on ...  *****
        if alist[j] > alist[max]:
            max = j

    # swap max and i
    alist[max],alist[i] = alist[i],alist[max]

print alist
