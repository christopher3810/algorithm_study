'''
- 문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
- 입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.
- 출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
'''
from pprint import pprint

'''
n - 회의 갯수
I - 각각의 회의
한번 시작하면 중간에 중단 불가능 한회의가 끝나는것과 동시에 다음 회의가 시작될수 있다.
회의 시작시간과 끝나는 시간이 같을 수도 있음 이건 시작하자마자 끝남 
- 코드
1. t = [list(map(int,input().split())) for _ in range(n)]
    이차원 리스트로 회의 시작값과 끝값을 받는다
2. t.sort(key=lambda x:(x[1],x[0]))
    회의가 끝나는 시간을 기점으로 람다식으로 정렬
3. end 변수에 회의가 끝나는 시간을 담고 시작하는 시간이 끝나는 시간보다 더 뒤거나 같은 상황을 기준으로 확인
'''
n = int(input())
t = [list(map(int,input().split())) for _ in range(n)]
count = 0
end = 0
t.sort(key=lambda x:(x[1],x[0]))
pprint(t)
for f,s in t:
    if (f >= end):
        end = s
        count += 1
print(count)
