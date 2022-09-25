# 이분 검색
# 임의의 N개의 숫자가 입력으로 주어집니다.
# N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면,
# 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.
# 단 중복값은 존재하지 않습니다.
# 입력설명
# 첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다. 두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.
# 출력설명
# 첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.

# n, t = map(int, input().split())
# listN = map(int, input().split())
# listN = sorted(listN)
# for index, n in enumerate(listN):
#     if t == n:
#         print(index+1)


# 이분검색은 맨왼쪽을 가르키는 lt가 필요하고 맨오른쪽 rt가 필요함
# lt 부터 rt까지 범위가 생김
# 이분검색은 mid = (lt+rt)//2 2로나눈 몪으로 갑니다
# 32 -> a[mid] == m 이면 index 가 0이니까 mid+1 하면됨
# a[mid] == m
# mid 기준으로 작다면 rt = mid-1
# mid 기준으로 크다면 lt = mid+1
# 한번만에 절반씩 작아지면 log2 1024 -> log n번만에 가능하다고 합니다.
# 이분 검색 전제조건은 정렬 상태
n, t = map(int, input().split())
listN =list(map(int, input().split()))
listN.sort()
lt = 0
rt = n-1
while lt <= rt:
    mid=(lt+rt)//2
    if listN[mid] == t:
        print(mid+1)
        break
    elif listN[mid]>t:
        rt = mid-1
    else:
        lt = mid+1
