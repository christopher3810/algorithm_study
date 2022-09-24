"""
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다.
그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.

10 13 10 12 15    10 13 10 12 15
12 39 30 23 11    23 11 12 39 30
11 25 50 53 15 -> 11 25 50 53 15
19 27 29 37 27    19 27 29 37 27
19 13 30 13 19    19 13 30 13 19

첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회 전하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.

입력설명
첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령 정보가 M줄에 걸쳐 주어집니다.
"""
"""
n = int(input())
listN = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
spinN = [list(map(int, input().split())) for _ in range(k)]

s = 0
e = n
total = 0

# list rearrange 를 어떻게 하냐 이게 중요함

for i in range(k):
    if spinN[i][1] == 0:  # 맨앞에 값이 맨뒤로 계속 이어서 붙음
        for j in range(spinN[i][2]):
            listN[spinN[i][0] - 1].append(listN[spinN[i][0] - 1][0])
            del listN[spinN[i][0] - 1][0]

    elif spinN[i][1] == 1:  # 맨 뒤에 값이 맨앞으로 붙음
        for j in range(spinN[i][2]):
            listN[spinN[i][0] - 1].insert(0, listN[spinN[i][0]-1][n - 1])
            del listN[spinN[i][0] - 1][n]  # 숫자가 한칸 밀리기 때문에 n을제거

for i in range(n):
    for j in range(s, e):
        total += listN[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(total)

"""

n = int(input())
listN = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:  # 왼쪽 방향 회전
        for _ in range(k):  # h-1행 index 값이기 때문에 -1해야함
            listN[h - 1].append(listN[h - 1].pop(0))
            # pop은 return 값이 있음 그리고 pop 하는순간 뒤에 자료들이 앞으로 땡겨짐 그리고 그 값을 맨뒤에다가 추가 하나의 회전 이 생김
    else:
        for _ in range(k):
            listN[h - 1].insert(0, listN[h - 1].pop(n - 1))
            # 맨뒤에서 꺼내서 맨앞에 insert 시킴

res = 0
s = 0
e = n - 1  # e의 값을 n-1로 할지 n으로 할지 정도의 차이
for i in range(n):
    for j in range(s, e + 1):
        res += listN[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
