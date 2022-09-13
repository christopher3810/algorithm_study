"""
스도쿠는 매우 간단한 숫자 퍼즐이다.
9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9 개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.

스도쿠를 정확하게 푼 경우는.
각 행에 1부터 9까지의 숫자가 중복 없이 나오 고,
각 열에 1부터 9까지의 숫자가 중복 없이 나오고,
각 3×3짜리 사각형(9개이며, 위에서 색 깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오는 경우이다.
완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.

▣ 출력설명
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

"""

# 3x3 마다 외벽을 0으로 초기화 떄려버림
# 그 리스트는 쓰고 버려
"""
listN = [list(map(int, input().split())) for _ in range(9)]
extraList = []
a = "YES"
for i in range(0, 9, 3):
    for j in range(0, 9):
        extraList.append(listN[i][j])
        extraList.append(listN[i + 1][j])
        extraList.append(listN[i + 2][j])
        if (j+1) % 3 == 0 :
            if len(extraList) != len(set(extraList)):
                a = "NO"
            extraList = []

print(a)
"""

"""
체크리스트가 3가지 필요함
행 ch 1~9 를 만들어놓고 돌면서 체크함 중복의 경우 ==1 로 넣기때문에 누적이아니라 그냥 1들어감
열 ch 1~9 를 만들어놓고 돌면서 체크함
sum(ch) == 9 리스트가 다 체크가 되어있으면 합산이 9여야함

"""


def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
                if sum(ch3) != 9:
                    return False
    return True


listN = [list(map(int, input().split())) for _ in range(9)]
if check(listN):
    print("YES")
else:
    print("NO")

"""
정리
일단 내가 문제를 잘못 풀음
1. 나는 그룹 체크만 했음 근데 전체 행 열 체크를 해야됬었던것

핵심정리
1. ch1 체크리스트를 활용해서 값을 1씩 넣은뒤에 sum을 활용하여 합산이 9인지를 체크
2. 행과 열을 체크
3. 4중 반복문을 활용해서 그룹 체크를 하는데 이부분이 중요함
3-1 일단 ch3 체크리스트 하나 확인
3-2
첫번쨰 반복문 i 는 아래로 3단위로 내려가는 숫자
0
1
2
--- 이렇게 3단위로 아래로 내려가는 i값
j는 옆으로 3단위로 늘려주는 값
0 1 2, 3 4 5, 6 7 8
i값을 3단위로 늘리니까 그 내부에서 3단위 내에서 0 1 2 돌아야 되고 j가 3단위로 돌거기 때문에 그 3안에서 0 1 2 돌아야 하기 때문에
반복문이 4가지나 필요한것 

3-2 : 즉 3단위로 행과 열을 돌기위해 i 와 j 가 필요하고 그 3단위 안에서 0 1 2 를 각각 돌기 위해서 k와 s가 필요한 것
j값이 바뀌고나서 리스트는 초기화
그러면 
왼쪽 위부터 3x3단위로 탐색을 수행한다.

"""