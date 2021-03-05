"""
For a given array of repeated elements, exactly one element is not repeated.
You need to return the non-repeated element.[1, 2, 5, 4, 6, 8, 9, 2, 1, 4, 5, 8, 9]

property of xor

n ^ n = 0

n ^ 0 = n
"""
arr = [1, 2, 5, 4, 6, 8, 9, 2, 1, 4, 5, 8, 9]
v = 0
for i in range(len(arr)):
  v = v ^ arr[i]
print(v)
#OUTPUT = 6