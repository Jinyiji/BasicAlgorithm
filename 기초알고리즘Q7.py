# 7.리스트에서 특정 원소만 추출하기
# ex)  [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서  2만 추출하기
# 리스트가 나오면 항상 포문을 써야한다

arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]
새로운공간 = list()

for x in arr:
	if x != 2:
		# 새로운 공간에 x를 넣는다.
		새로운공간.append(x)
print(새로운공간)

