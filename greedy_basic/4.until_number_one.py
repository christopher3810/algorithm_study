"""
문제
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단 두 번쨰 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번ㄷ의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.
- 입력조건 : 첫째 줄에 N(2 ≤ N ≤ 100,000)과 K(2≤ K ≤ 100,000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
- 출력조건 : 첫쨰 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
"""

n, k = map(int, input().split())
result = 0;

# n의 값이 k의 값보다 큰경우의 루프
# n = 25 k = 3 n의 값이 2 와 1이 된 경우는 따로 처리를 해줘야함
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

# 위의 연산을 거치고 남은 수에 대해서는 더이상 나누지를 못하고 1까지 뺼셈 진행해야 함.
while n > 1:
    n -= 1
    result += 1

print(result)


"""
두번쨰 방법
"""

q, t = map(int, input().split())
result2 = 0;

while True:
    # taget n으로 k를 딱 나눠 떨어지게 하는 숫자 나눗셈을 시작할 수 있는 타겟 수자
    target = (q//t) * t
    # 전체에서 타겟숫자를 빼면 -1 씩 진행할 횟수가 나옴
    # result 에는 첫 나눗셈 지점 전까지 -1을 할 횟수가 이미 더해짐
    result += (q - target)
    q = target
    # N이 K보다 작을때 더이상 나눌수 없을때 반복문 탈출
    if q < t :
        break
    # k로 나누기
    result += 1
    q //= t

# -1 을 함으로서 1이 되기전까지 -1을 할 횟수를 계산
# EX) Q 4 T 5 더이상 나눌수 없어서 나오면 4가 1이 되기까지 3번을 -1 해야됨 -1로 1을 확보한 나머지 횟수를 바로 계산 4-1
result += (q - 1)
print(result)