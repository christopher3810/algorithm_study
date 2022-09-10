"""
격자판 최대합
5*5 격자판에 아래와 같이 숫자가 적혀있습니다.
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

▣ 출력설명
최대합 출력

▣ 입력예제 1
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

▣ 출력예제 1
155

"""
'''
#내풀이
n = int(input())
listN = [list(map(int, input().split())) for _ in range(n)] #range 로 돌아서 2차원 배열로 받음
maxNum = -21740000
listT = [0] * n #특정 크기만큼 0으로 초기화
cntReverse = n-1
leftCross = 0
rightCross = 0

for i in range(n):
    rowSum = 0
    leftCross += listN[i][i]
    rightCross += listN[i][cntReverse]

    if maxNum < sum(listN[i]):
        maxNum = sum(listN[i])

    for j in range(n):
        rowSum += listN[j][i]

        if maxNum < rowSum:
            maxNum = rowSum

    cntReverse -= 1

if maxNum < leftCross:
    maxNum = leftCross

if maxNum < rightCross:
    maxNum = rightCross

print(maxNum)
'''

# 풀이
n = int(input())
# map(int, input().split()) 한줄을 map을 통해서 읽어듦임
# a = [list(map(int, input().split()))] 한줄을 읽어서 list 화 까지 시킨것
a = [list(map(int, input().split())) for _ in range(n)]  # 한줄을 읽어서 list화 시킨것을 n 번하는것
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    # 0으로 초기화
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
        # 행과 열을 합함
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
print(largest)

'''
정리
1. 변수를 필요에 따라서 생성하지 말고 전역생성후에 로직처리후 초기화시킨다음 재활용하자
2. 오른쪽 끝 부터 왼쪽 끝까지 내려오야 하는 경우 고정된 n값과 증가하는 i값을 활용하여 계산하자 단 N은 인덱스 +1 이기 때문에 
   -1을 꼭 붙여주도록 하자 -> n-i-1

'''
