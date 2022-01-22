def solution(lottos, win_nums):
    """
    1. lottos와 win_nums 비교 하여 일치하는 숫자 갯수 확인.
    2. lottos 내의 0의 갯수 확인.
    3. 최대는 일치하는 숫자 + 0의 갯수, 최소는 일치하는 숫자.
    """
    #lottos와 win_nums의 교집합 구하기.
    set_lottos = set(lottos)
    set_winnums= set(win_nums)
    intersection_num = len(list(set_lottos & set_winnums))
    # lottos 내의 0의 갯수 확인.
    zero_num = lottos.count(0)
    #당첨 갯수
    winning_max = 7 - (intersection_num + zero_num)
    if intersection_num == 0:
        winning_min = 6
    else:
        winning_min = 7 -intersection_num
    winning_max = min(winning_max,6) #winning_max가 6보다 크면 6을 반환한다.
    answer = [winning_max, winning_min]
    return answer
