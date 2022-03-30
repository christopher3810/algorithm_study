'''
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면
YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

▣ 입력설명
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.
▣ 출력설명
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

▣ 입력예제
5
level
moon
abcba
soon
gooG

▣ 출력예제
#1 YES
#2 NO
#3 YES
#4 NO
#5 YES
'''

# 1. 반복을 전체에서 몫 만큼만 도는것 -> 홀수 여도 반 짝수여도 반
# 2. 비교를 lower() 를 통해서 소문자로 전환해서 대소 구분을 하지않고 맞는 문자인지 확인하는것
def checkPalin(listN):
    for i in listN:
        for j in range(0, len(i) // 2):
            if i[j].lower() != i[len(i)-1 - j].lower():
                return False
    else:
        return True


n = int(input())
listN = [list(map(str, input().split('\n'))) for _ in range(n)]

for index, value in enumerate(listN):
    if checkPalin(value):
        print("#" + str(index+1) + ' YES')
    elif not checkPalin(value):
        print("#" + str(index+1) + ' NO')

'''
n = int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2): #리스트 인덱스는 -1 -2 -3 -4- 5 이런식으로가면 뒤로부터 역순으로 가는것 -1 이 맨뒤 
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
        
    #더 짧도록
    if s == s[::-1]: # [::-1]리버스 한것 파이썬 할때도 중요하지만 직접 구현하는것도 중요함 
        print("#%d YES" %(i+1))
    else :
        print("#%d NO" %(i+1))
'''