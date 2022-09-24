"""
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면
격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

8 7 1 7
      8
구부러 졌기 때문에 회문수로 간주하지 않습니다.


▣ 입력설명
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.
▣ 출력설명 5자리 회문수의
▣ 입력예제 1 2415326 3518717 8327138 6123211 1313532 1125652 1222215
▣ 출력예제 1 3
개수를 출력합니다.

"""

# listN = [list(map(int, input().split())) for _ in range(7)]
#
# count = 0
# hlist = []
# vlist = []
#
# for i in range(7):
#     for k in range(3):
#         for j in range(5):
#             hlist.append(listN[i][j + k])
#             vlist.append(listN[j + k][i])
#
#         htemp = 0
#         vtemp = 0
#         templist = [4,3]
#         for l in range(2):
#             if hlist[l] == hlist[templist[l]]:
#                 htemp += 1
#             if vlist[l] == vlist[templist[l]]:
#                 vtemp += 1
#         if vtemp == 2:
#             count += 1
#         elif htemp == 2:
#             count += 1
#         hlist = []
#         vlist = []
# print(count)
# 반복문 3개사용, 변수6개사용.. 좀 극혐
# 세번 째 반복문은 리스트 슬라이스로 대체 가능


listN = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = listN[j][i:i+5]
        if tmp == tmp[::-1]:
           cnt += 1  #아래로 내려가는 애들은 슬라이스가 불가능 하기 대문에 for 문 돌긴 해야됨
        for k in range(2):
            if listN[i+k][j] != listN[i+5-k-1][j]:
                # i = 0 인것부터 아래로 내려감
                # i + 5 - k -1
                # 5-> 회문 길이, i 는 비교 시작 지점 (0,1,2)총길이 7이니까 3개만 비교하면됨
                # k -> 맨뒤에서부터 한칸씩 내려오면서 비교하고싶어서 넣은 감산 연산자 예가 증가하면서 맨뒤에서부터 한칸씩 땡겨짐
                # -1 -> 리스트 인덱스가 0~4 까지이기 때문에 최초 비교자리인 5에서는 -1 을 해서 4로 맞춰줘야함
                # i + k =
                break
        else:
           cnt += 1
        #회문을 확인하는 증감자 cnt 사이에 조건문을 넣고 break 걸어서 아닌겨우에 한해서 카운트르 안하는 방식
print(cnt)