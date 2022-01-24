from collections import Counter

def solution(N, stages):
    fail_rate = {} #실패율
    user_num = len(stages) #참여자 수
    #스테이지 별 클리어하지 못한 플레이어 수를 dict화
    cnt = Counter(stages)
    for i in range(N):
        user_in_stage = cnt[i+1]
        if user_in_stage > 0:
            fail_rate[i+1] = user_in_stage/user_num
            user_num -= user_in_stage
        elif not user_in_stage:
            fail_rate[i+1] = 0
        else:
            pass
    answer = sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True)
    return answer
