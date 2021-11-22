# 2.원소의 갯수를 카운터하기
# ex) [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서  2의 갯수를 카운팅

arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]
count = 0

for x in arr:
    if x == 2:
        count += 1

print(count)