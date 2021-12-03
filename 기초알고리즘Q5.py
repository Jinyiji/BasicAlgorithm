# 5.빈 리스트에서 기존의 값들보다 큰 값이 추가될 때마다 카운팅
# ex) 빈 리스트에서 [1, 3, 2, 6, 4, 9, 5]가 추가되는 상황
# ex) “ILOVKEFLOVEE”에서 “LOV”가 몇개 있는지 카운팅

string = "ILOVKEFLOVEE"

count = 0
for i in range(len(string)):
    # 첫 글자가 "L"인 경우
    if string[i] == "L":
        # 두 번째 글자가 "O"인 경우
        if string[i+1]  == "O":
            # 세 번째 글자가 "V"인 경우
            if string[i+2] == "V":
                # 카운팅
                count += 1
print(count)
