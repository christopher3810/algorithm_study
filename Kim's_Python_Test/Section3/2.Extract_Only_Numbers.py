'''
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.즉첫자리0은자연수화할때무시합니다.
출력은120를출력하고,다음줄에120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

▣ 입력설명
첫 줄에 숫자가 석인 문자열이 주어집니다.
문자열의 길이는 50을 넘지 않습니다.

▣ 출력설명
첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.

▣ 입력예제
g0en2Ts8eSoft

▣ 출력예제
28
6

'''
# 45 ~ 57

n = str(input())
result = ''
for i in n:
    if 48 <= int(ord(i)) <= 57:
        result += i
number = int(result)
cnt = 1 #자기자신
for i in range(1, int(number/2 + 1)) :
    if number % i == 0 :
       cnt += 1
print(number, cnt, sep='\n')

'''
# digit 2^2 , 2^31 이런거 들어와도 인식함
# decimal 은 0~9까지
s=input()
for x in s:
    if x.isdecimal():
        res=res*10+int(x) # 0dp 10곱해서 계속 더해봤자 무시됨 최고지리에 0을 무시함
print(res)
cnt = 0
for i in range(1, res+1):
    if res%i ==0:
        cnt +=1
print(cnt)

'''