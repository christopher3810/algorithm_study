'''
N명의 학생의 수학점수가 주어집니다.
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
높 은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다.
학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.

입력 예제
10
45 73 66 87 92 67 75 79 75 80

출력 예제
74 7

'''
from math import ceil

# 최소거리를 찾고 리스트에서 최소거리에 있는 인덱스를 찾아서 소팅해서 출력;;; 비효율적 ... 최대한 그냥 지역변수 사용해서 간단하게 짜자;;
t = int(input())
a = list(map(int, input().split()))
aver = round(sum(a) / len(a))
minValue = 2147000000
totalList = []
for index, value in enumerate(a) :
    if minValue >= abs(aver - value):
        minValue = abs(aver - value)
for index, value in enumerate(a) :
    if minValue == abs(aver - value) :
        totalList.append([value, index+1])
totalList.sort(key=lambda x:-x[0])

print("%d %d" % (aver, totalList[0][1]))

'''
# 이런식으로 그냥 한번의 순회에서 반복없이 조건문만으로 출력 
t = int(input())
a = list(map(int, input().split()))
ave=round(sum(a) / n)
for idx, value in enumerate(a) :
    temp=abs(x-ave)
    if temp<min:
        min=tml
        score=x
        res=idx+1
    elif tmp == min:
        if x>score: # 73 75 75 75 75 뒤에 75들은 score 가 크지 않기 때문에 그냥 사용 
            score=x
            res=idx + 1 
'''