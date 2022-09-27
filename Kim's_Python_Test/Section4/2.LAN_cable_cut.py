# 엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이 다.
# 선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
# 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
# 편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
# 그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
# 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
# 입력설명
# 첫째 줄에는 엘리트학원이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다.
# K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다.
# 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의   이하의 자연수로 주어진다.
# 출력설명
# 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
#
# 입력예제
# 4 11
# 802
# 743
# 457 539
#
# 출력예제
# 200
# n, t = map(int, input().split())
# listN = list(int(input()) for _ in range(n))
#
# lt = 0
# rt = sum(listN)
#
# def count(linstN, mid):
#     cnt = 0
#     for element in linstN:
#         cnt += element // mid
#     return cnt
#
# templist = []
# while lt <= rt:
#     mid = (lt + rt) // 2
#     if count(listN, mid) == t:
#         templist.append(mid)
#         lt = mid + 1
#     elif count(listN, mid) > t:
#         lt = mid + 1
#     else:
#         rt = mid - 1
#
# print(max(templist))
# # 이경우에는 몇개 통과 못하미;;


"""
이분 검색 찾고자 하는 답이 특정 범위 안에 있다 라는 것을 바로 알수가 있다.
몇 부터 몇사이에 답이 있다 라는 것을 알 수 있음.
범위내에서 특정 숫자를 정해놓고 중앙값을 정해놓고 이분 검색을 실행함
중앙값을 정해두고 그 값이 답으로써 유효하냐 안 유효하냐 확인작업을 함
이게 답이 된다 그러면 범위를 좁히고 절반을 날리고 남은 절반중에서 이 답보다 더 좋은 답을 찾아서 좁혀 나가는 방식

n개의 랜선을 만들수 있으면서 각각의 n개의 랜선을 최대로 해서 만들어라

찾아나가는 방법론
n개의 랜선 한개의 길이는 1~ 가장 큰 랜선 길이
1 ~ 802
이범위에서 이분탐색을하면서 값을 뽑고
802
743
457
539
를 돌면서 몫값을 돔
그리고 몫을 더해서 주어진 값과 비교를하면서 범주를 계속 조절해서 내려감
그리고 구해진 값을 기준으로 최소 값기준을 잡아서 범주 탐색을 다시함
예를들어서
1~249 라는 범주에서
125라는 값이 있으면
125라는 값을 최소값으로 범주를 다시 설정하고
125 ~ 249
이범주내에서 다시 확인함
최대 값을 구해야 하기 때문
그러면 187이라는 답이 생김
187 ~ 249 이렇게 올림
"""
def count(len):
    cnt = 0
    for x in line:
        cnt += (x//len) # 각각의 랜선길이에서 mid 로 나눈 몫 -> 토막의 갯수
    return cnt


n, t = map(int, input().split())
line = []
res = 0
largest = 0
for i in range(n):
    tmp = int(input())
    line.append(tmp)
    largest=max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:
    mid =(lt + rt) // 2
    if count(mid) >= n: #값이 되는지 안되는지 판정해주는 함수
        res=mid #임시 정답 변수에 값을 넣음
        lt = res
    else:
        rt = mid -1 #긴쪽은 다 버려야 되기 때문에 rt 가 바뀌어야 한다.

print(res)