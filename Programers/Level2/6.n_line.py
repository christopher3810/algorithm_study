import math
from itertools import permutations

n = 4
k = 7


#factorial 을 사용해서 경우의 수를 구한다 3! -> 6개 // 3 으로하면 앞이 1인애들 2개 2인애들 2개 3인애들 2개 5 -> 3번째에 첫번쨰
#이와같이 탐색돌 구간을 정해서 돈다


def solution(n, k):
    # 줄서는 사람
    people = [_ for _ in range(1, n + 1)]
    # 답을 넣을 리스트
    answer = []
    while (n != 0):
        # 한 사람이 앞에 줄을 섰을 때의 경우의 수
        each_first_cases = math.factorial(n) // n
        # k번째를 구하기 위해 한 사람이 앞에 줄을 섰을 때의 경우의 수를 지나간 수
        passed = k // each_first_cases
        # 나머지를 k에 넣기
        k = k % each_first_cases
        if k == 0:
            answer.append(people.pop(passed - 1))
        else:
            answer.append(people.pop(passed))
        n -= 1
    return answer


solution(n, k)
