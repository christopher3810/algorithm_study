# DFS 와 BFS를 이해하고 활용하기 위해선
# python내에서 stack을 어떻게 활용할 수 있을지 생각해 봐야 한다.

# stack은 선입후출 first in last out 또는 후입 선출 last in first out 구조 라고 한다
# 별도의 라이브러리 사용할 필요없이 리스트에서 사용가능
stack = []

# 5 - 2 - 3 - 7 - pop - 1 - 4 - pop
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력

"""
출력 값
5 , 2, 3 , 1
1, 3 ,2 , 5
"""
