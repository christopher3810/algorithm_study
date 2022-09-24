"""
봉우리
지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다.
각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.

▣ 출력설명
봉우리의 개수를 출력하세요.

▣ 입력예제
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2

▣ 출력예제
10

"""

"""
n = int(input())
listN = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
l=r=t=b=0
zero = [0] * n
listN.insert(0,zero)
listN.append(zero)
for i in listN:
    i.insert(0,0)
    i.append(0)
# 2차원 배열에서 2번쨰부터 돌기
for i in range(1, len(listN)):
    for j in range(1, len(listN)):
        if listN[i][j] > listN[i][j-1] and listN[i][j] > listN[i][j+1]:
            if listN[i][j] > listN[i-1][j] and listN[i][j] > listN[i+1][j]:
                cnt += 1
print(cnt)
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
listN = [list(map(int, input().split())) for _ in range(n)]
listN.insert(0, [0] * n)
listN.append([0] * n)
for x in listN:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(listN[i][j] > listN[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

"""
봉우리 문제 요지
a. 벽으로 막힌 왼쪽 위 아래 오른쪽 에 해당하는경우 0으로 비교를 할 수 있는가
b. 4방향 탐색을 해서 어떻게 비교할 것인가

봉우리 문제 해결안
1. 2차원 배열 외부를 0으로 다 초기화 해버린다.
insert를 통해서 0으로 초기화된 배열을 맨위에 넣고
append를 통해서 0으로 초기화된 배열을 맨 아래에 넣는다
반복문을 돌면서 insert와 append를 통해서 배열 앞뒤에 0을 넣어준다
2. all() 메서드를 활용해서 모든 조건이 참일때 참을 반환하도록 한다
3. dx = [-1 ,0 ,1 ,0] , dy = [0, 1, 0, -1] 리스트 dx와 dy를 활용하여 상 하 좌 우 를 탐색하도록 한다
    움직일 방향에대한 좌표값들을 미리 넣어두고 반복문을 통해서 돌도록 하는 로직
listN[i + dx[k]][j + dy[k]] for k in range(4)
i값과 y값을 리스트에 있는 값으로 이동시키면서 상하좌우를 탐색한다.

정리 : 0으로 초기화 하여 위 아래 좌 우 에 벽을 0으로 막아서 예외처리 없애기, all메서드를 통해서 조건문 간략화, dx,dy를통해서 2차원 배열내에 탐색 방향
미리 지정해두고 반복문을 통해서 이동후 조건문 확인.
"""