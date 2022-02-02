import re

p = re.compile('[0-9]*[SDT][*#]?') #정규식을 통해 분리

def solution(dartResult):
    char = {"S":1, "D":2, "T":3}
    num = {}
    m = p.findall(dartResult)
    for count, value in enumerate(m):
        num[count] = 0
        for j, i in enumerate(value):
            if i.isdigit():
                if value[j-1].isdigit():
                    num[count] = 10
                else:
                    num[count] = int(i)
            elif i.isalpha():
                num[count] = num[count]**char[i]
            else:
                if i == "*":
                    if count > 0:
                        num[count-1] = num[count-1]*2
                        num[count] = num[count]*2
                    else:
                        num[count] = num[count]*2
                else:
                    num[count] = num[count]*-1
    answer = num[0]+num[1]+num[2]

    return answer
