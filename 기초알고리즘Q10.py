# 10.최대값 혹은 최소값을 구하는 알고리즘 직접 구현하기(max, min함수 쓰지 않고)

arr = [3, 6, 2, 7]
최대값 = arr[0]

for x in arr:
	if 최대값 < x:
		최대값 = x

print(최대값)

