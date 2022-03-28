'''
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요.
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 10,000,000를 넘지 않는다.
▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자 를 출력합니다.
▣ 입력예제
3
125 15232 97
▣ 출력예제
97
'''
n = int(input())
listN = list(map(int, input().split()))
maxmum = -21700000
total = []


def digit_sum(x):
    global maxmum
    sd = 0
    for i in str(x):
        sd += int(i)
    if maxmum < sd:
        maxmum = sd
    return sd


for i in range(0, n):
    total.append(digit_sum(listN[i]))
print(listN[total.index(maxmum)])

'''
n = int(input())
listN = list(map(int, input().split()))

def digit_sum(x):
    sum=0
    while x > 0:
        sum += x%10 #125 10 으로 나눈 나머지 5
        x=x//10 # 10으로 나눈 목 12
        # 125 -> 한회차때 5, 12 , -> 1 , 0 
        # 이런 방식도 있다

for x in listN:
    tot = digit_sum(x) #합 리턴
    if tot>max :
        max = tot
        res = x

print(res)
# if 문에서 max 값이 클때 로 걸러서 res 값으로 저장해놓으면 그이후에 오는것들은 거르기 떄문에 맨처음 발견한 값만 리턴 가능
'''
