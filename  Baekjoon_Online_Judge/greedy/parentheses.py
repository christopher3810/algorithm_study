'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.

예시
55-50+40
-35

생각
일단 딱봐도 +는 의미가 없고
-인경우가 중요한데
-로 split 해서 쪼개논다음에
10 + 20 - 30 - 40 + 50
10+ 20 , 30 , 40+ 50
맨처음 빼고 나머지다 - 붙여서 연산하면 끝
1. 스트링으로 입력 받는다
2. spit -
3. 연산
'''
'''
s = input().split('-')
result = 0
if len(s) > 1:
    for i, v in enumerate(s):
        if i == 0:
            if "+" in v:
                temp = v.split("+")
                for i in temp:
                    i.lstrip("0")
                    result += int(i)
            else:
                result += int(s[0].lstrip("0"))
        else:
            if "+" in v:
                temp = v.split("+")
                for i in temp:
                    i.lstrip("0")
                    result -= int(i)
            else:
                result -= int(v.lstrip("0"))
    print(result)
if len(s) == 1:
    if "+" in s[0] :
        temp = s[0].split("+")
        for i in temp:
            i.lstrip("0")
            result += int(i)
        print(result)
    else:
        print(int(s[0]))
'''
# 초키 로직코드 작성
# lstrip을 사용할 필요가 없음
# sum()사용시 리스트 합산에서 009의 형태도 계산해서 보여줌
# 1. 맨처음 숫자를 덧셈 처리하고
# 2. 이후 숫자들을 +를 쪼개서 리스트로 만든뒤 리스트 전체 합산값으로 만들어준뒤 뺄셈
# 개선코드

a = input().split('-')
# 맨 앞자리 숫자는 덧셈처리 해야하니 전체 리스트에서 맨앞 pop으로 뺀뒤 스플릿해서 전체 합(- 스플릿한 첫번쨰 수는 한가지일수도 연산식일수도 있다.)
s = sum(list(map(int, a.pop(0).split('+'))))
for x in a :
    s -= sum(list(map(int, x.split('+'))))
    # 나머지 숫자 + 기준으로 스플릿후 리스트로 만든뒤 리스트 전체 한산값 - 붙여줌
print(s)
