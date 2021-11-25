# 4.Bubble Sort 구현

arr = [8, 5, 6, 3, 4]
for i in range(0, len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# len(arr) : 5
# j: len(arr) -i - 2:
# i:0	j: 0, 1, 2, 3
# i:1	j: 0, 1, 2
# i:2	j: 0, 1
# i:3	j: 0
