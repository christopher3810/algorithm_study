# 지니레코드에서는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다.
# DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지 되어야 한다.
# 순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다.
# 즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야 한다.
# 또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
# 지니레코드 입장에서는 이 DVD가 팔릴 것인지 확신할 수 없기 때문에 이 사업에 낭비되는 DVD를 가급적 줄이려고 한다.
# 고민 끝에 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기 로 하였다. 이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다.
# 그리고 M개의 DVD는 모두 같은 크기여야 제조원가가 적게 들기 때문에 꼭 같은 크기로 해야 한다.
#
# 입력설명
# 첫째 줄에 자연수 N(1≤N≤1,000), M(1≤M≤N)이 주어진다. 다음 줄에는 조영필이 라이브에서 부른 순서대로 부른 곡의 길이가 분 단위로(자연수) 주어진다.
# 부른 곡의 길이는 10,000분을 넘지 않는다고 가정하자.
#
# 출력설명
# 첫 번째 줄부터 DVD의 최소 용량 크기를 출력하세요.
#
# 입력예제
# 9 3
# 1 2 3 4 5 6 7 8 9
#
# 출력예제
# 17


# 범위가 뭐가 있을까 먼저 정리를 해보자
# lt rt 에대한 범위를 어떤걸로 어떻게 잡을까?
# rt = 합연산이 맞음 1개가 걸리면 합연산으로 하나만 넣어야함
# lt = 가장 큰값 -> dvd가 여러개라고 한다면 가장큰값이 되어야 함
# 판별 함수 로직
# dvd 용량 최소 용량부터 최대 용량 까지 범주 내에서 합연산으로 맞는게 몇개가 되는지 확인해야함
# 1 1 1 1 1 -> 1 1 1 1 1 1 3-> 4


# def count(time):
#     total = 0
#     cnt = 1
#     for i in listN:
#         if total + i > time:
#             total = i
#             cnt += 1
#         else:
#             total += i
#     return cnt
#
#
# n, k = map(int, input().split())
# listN = list(map(int, input().split()))
# lt = max(listN)
# rt = sum(listN)
# res = 0
# while lt <= rt:
#     mid = (lt + rt) // 2
#     if count(mid) <= k:
#         res = mid
#         rt = mid - 1
#     else:
#         lt = mid + 1
# print(res)

"""

포인트
주어진값이 9 와 3

lt  rt
1   45

mid = 23
3장만에 됬다 그래서 답이 됨
res = 23

dvd 용량이 량이 2장만에 됬다면 답이 아닌가?
두장만에 다 저장이 되더라 9곡이 그러면 답이아닌가?
당연히 답이됨 2장에 되면 3장에 당연히 저장이됨

최소값을 구해야 하기때문에 23-1을 rt값으로 주자
lt  rt
1   22

mid = 11
최소 5장
11이하는 필요가없음 5장 이상이 될 것이기때문에 이하 값은 버린다

lt rt
11 22

반복
"""

# k값이 list 전체 길이와 동일하면 에러발생함
def count(capacity):
    cnt = 1
    total = 0
    for x in listN:
        if total + x > capacity:  #total 에다가 값을 무조건 집어 넣 새로운 dvd 에다가 노래를 무조건 넣는다 즉 리스트 그어떤 요소보다 capacity보다 크거나 같아야함
            cnt += 1
            total = x # 왜냐면 적어도 하나는 담을수 있어야 하기 때문에
        else:  # 초과 안됬으면 저장 가능
            total += x
    return cnt


n, k = map(int, input().split())
listN = list(map(int, input().split()))
lt = max(listN)
rt = sum(listN)
maxx = max(listN) # dvd의 용량은 최소한 listN요소중 가장 큰 값을 수용할수 있어야함 왜냐면 개당 한개씩을 무조건 넣을수 있어야 하기 때문에
res = 0
while lt < rt:
    mid = (lt + rt) // 2
    if mid >= maxx and count(mid) <= k:
        # 2장만에 다 저장 되더라 -> 이건 답이 되는것
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)

"""
99 와같이
dvd 가 개당 한개의 노래를 담아야되는 범위로 변경이되면 -> capacity로 넘어가는 중간값이
listN의 리스트 요소들중 가장 큰 값 보다 작아져 버리면 예를들면 리스트요소인 9 보다 작은 8이라는 capacity가 함수로 전달이되면
해당 노래를 dvd는 담을수가 없게됨 그래서 패스하게되고
값이 이상하게 나오게됨 논리적으로 문제가 존재.
"""