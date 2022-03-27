'''
두 개의 정 N 면체와 정 M 면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
▣ 출력설명
첫 번째 줄에 답을 출력합니다.
▣ 입력예제 1
46
▣ 출력예제 1
567
'''
#list 한가지를 활용하여 인덱스와 value 값으로 한한 값과 경우의수를 저장하기
n, m = map(int, input().split())
listN = list(range(1, n+1, 1))
listM = list(range(1, m+1, 1))
total = []
for i in listN:
    for j in listM:
        total.append(i + j)
uni = set(total)
max = 0
result = []
for i in uni :
    if max < total.count(i):
        result.clear()
        max = total.count(i)
        result.append(i)
    elif max == total.count(i):
        result.append(i)
result.sort()
for i in result : print(i, end = " " )

'''
# 리스트 하나를 활용해서 Index 값이 합산값 value 값이 등장한 횟수로 활용
n, m = map(int, input().split())
cnt = [0]*(n+m+3) # 눈의 합은 n+m 이상은 나오지 않기 때문에 하지만 예외때문에 넉넉하게 +3 0으로 초기화된 경우의수 리스트 생성
max = -2147000000
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1 # i+j 를 인덱스로 활용하고 값을 증감시켜준다
for i in range(n+m+1):
    if cnt[i] > max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i] == max :
        print(i, end = ' ')
'''