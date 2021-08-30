"""
문제
배열의 크기 n, 숫자가 더해지는 횟수 m, 그리고 k가 주어질 때 성민이의 큰 수의 법칙에 따른 결과를 출력 하시오
입력조건
첫째 줄에 n(2 ≤ n ≤ 1000), m(1 ≤ m ≤ 10,000), k(1 ≤ k ≤ 10,000)의 자연수가 주어지며 각 자연수는 공백으로 구분한다
둘째 줄에 n개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의
자연수는 1이상 10,000 이하의 수로 주어진다.
입력으로 주어지는 k는 항상 m보다 작거나 같다.
"""

# n, m , k 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수들 정렬하기.
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
