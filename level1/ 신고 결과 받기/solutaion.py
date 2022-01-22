def solution(id_list, report, k):
    #id_list를 dict로 변환
    id_dict = {string:0 for string in id_list}
    #신고당한 유저를 key, 신고한 유저들을 value로 가진 dictionary 생성
    dict_report = {string:[] for string in id_list}
    #set 함수를 이용하여 동일한 유저에 대한 신고 횟수 1회로 변경
    onetime_report = set(report)
    for i in onetime_report:
        split_report=i.split() #신고 레포트를 " "기준으로 분할
        dict_report[split_report[1]].append(split_report[0]) #분할 한 것을 dict에 담기.
    for i in id_list:
        if len(dict_report[i])>=k: #신고한 사람들 숫자가 k보다 크면 id_list의 신고한 사람 숫자 1증가.
            for j in dict_report[i]:
                id_dict[j]+=1
    #id_dict의 value들을 list로 변환
    answer = list(id_dict.values())
    return answer
