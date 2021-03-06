"""
문제
거스름돈으로 사용할 500원 100원 50원 10원 짜리 동전이 무한히 존재한다고 가정할시
손님에게 거슬러 줘야할 돈이 n원일 때 거슬러줘야 할 동전의 최소 갯수를 구하라.
단 거슬러 줘야 할 돈 n은 항상 10의 배수이다.
"""

n = 1200
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += 1  # 책 원문은 오타임 갯수를 새는 카운트를 증감시키고
    n %= coin  # 입력값 금액을 리스트에있는 요소로 나눈 나머지를 갱신시킴

print(count)  # 받을수 있는 가짓수를 출력해줌
