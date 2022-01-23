from itertools import combinations

def solution(nums):
    answer = 0
    """
    1000이하의 자연수가 있으므로 최대 합은 3000이하이다.
    54^2이 2916이므로, 54 이하의 소수를 알면 3000까지의 소수를 구할 수 있다.
    54이하의 소수로 3000까지의 수를 나눠서 나머지가 0이 아닌 숫자는 소수.
    """
    #54까지의 존재하는 소수 구하기
    sosus = list(range(2,55))

    for i in [2,3,5,7]:
        sosus = sosuRemove(sosus, i)
    sosus += [2,3,5,7]
    sosus.sort()

    #세 수 조합 구하기
    comb = combinations(nums, 3)

    comb_sum = [sum(i) for i in comb]

    for sum_result in comb_sum:
        for sosu in sosus:
            # 54 이하의 소수이면 +1
            if sum_result == sosu:
                answer +=1
                break
            #합이 54 이하의 소수로 나눠지면 소수가 아니므로 멈춤.
            elif sum_result % sosu == 0:
                break
            #합이 54이하의 소수로 나눠지지 않으면 소수이므로 +1
            elif sum_result > sosus[-1] and sosus[-1] == sosu:
                print(sum_result % sosu, sosu)
                answer +=1
                break
            else:
                pass

    return answer


def sosuRemove(arr, num):
    for i in arr:
        if i % num == 0:
            arr.remove(i)
    return arr
