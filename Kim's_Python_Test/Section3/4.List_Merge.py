'''
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.
▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.

▣ 입력예제
3
135
5
23679

▣ 출력예제
12335679
'''

n = int(input())
m = list(map(int, input().split()))
l = int(input())
k = list(map(int, input().split()))

m.extend(k)
m.sort() #sort 는 시간 복잡도가 nLogN (sort는 퀵정렬은 가장 빠름)
for i in m:
    print(i, end = ' ')

'''
근데 이미 데이터가 정렬이 되어있으면 n log n이아니라 n번만에 가능
    p1
a : 0 1 2 3
    1 3 5

    p2
b : 0 1 2 3 4 5
    2 3 6 7 9

if a[p1] < b[p2]
a의 인덱스 지정 포인터 p1을 증가시켜줌
else
b의 인덱스 지정 포인터 p2을 증가시켜줌
둘중의 하나가 끝나면 나머지 배열의 뒤에것을 slice로 붙여주면 됨 

n = int(input())
a= list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c=[]
while p1<n and p2<m:
    if a[p1] <= b[p2] :
        c.append(a[p1])
    else : 
        c.append(b[p2])
if p1<n
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end = ' ')
'''