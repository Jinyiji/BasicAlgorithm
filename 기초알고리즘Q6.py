# 6.어떤 문자열에 해당단어가 몇개있는지 카운팅
# ex) ILOVKEFLOVEE에서 LOV가 몇개 있는지 카운팅

string = "ILOVKEFLOVEE"

find="LOV"
print(string.count(find))

count = 0
for i in range(len(string)):
    #첫 글자가 "L"인 경우 and 찾아야하는 끝 글자의 범위체크
    if string[i] == find[0] and i+len(find) <= len(string):
        # 첫 글자가 "O"인 경우
        if string[i+1] == find[1]:
            # 첫 글자가 "V"인 경우
            if string[i+2] == find[2]:
                count += 1
