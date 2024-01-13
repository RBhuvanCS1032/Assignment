arr = [3,1,2,5,3]
arr.sort()
repeat = 0
miss = 0
for i in range(len(arr)):
    if i == len(arr)-1:
        break
    if arr[i] == arr[i+1]:
        repeat = arr[i]
    if arr[i+1] - arr[i]!= 1:
        miss = i+1
print("Missing:",miss,"Repeating:",repeat)