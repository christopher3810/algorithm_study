'''
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다.
같은 숫자의 카드가 여러장 있을 수 있습니다.
현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려 고 합니다.
3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.
▣ 입력설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 된다.
▣ 출력설명
첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.
▣ 입력예제
10 3
13 15 34 23 45 65 33 11 26 42
▣ 출력예제
143
'''
from itertools import permutations

# itertools 를 활용한 방법
size, index = map(int, input().split())
sortedList = list(map(int, input().split()))
totalList = []
for data in list(permutations(sortedList, 3)):
    data: tuple = data
    sumData = sum(data)
    totalList.append(sumData)
totalList = list(set(totalList))
totalList.sort(reverse=True)
print(totalList[index - 1])

'''
1. 3중 for문을 활용한 방법
n, k = map(int, input().split())
a = list(map(int, input().split()))
# list 에 계속 append를 하면 중복이되기 때문에 set이라는 자료구조를 사용해서 중복 제거를 한다
res=set()
for i in range(n):
    for j in range(i+1, n): # i 바로 뒤에 자료 가져오기 i 위치와 j 의 중복을 막기위해 i 기준으로 뒤
        for m in range(j+1, n): #j 뒤 바로 m과 j의 중복을 제거하기위해 j 기준으로 뒤
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
'''