### min(), max()
***
- 인자로 리스트를 전달해도 되고 객체들을 인자로 전달할 수 있음 .
```python
numbers = [5, 4, 1, 2, 3]

result = min(numbers)
print(result)

result = min(5, 4, 1, 2, 3)
print(result)

#가장 작은 값 반환
```
- 문자열 리스트의 최소, 최대의 경우 ASCII 값을 비교하여 가장 낮은 값이 최솟값이 됨.
```python
fruits = ['watermelon', 'kiwi', 'blueberry', 'apple']

print(min(fruits))
print(max(fruits))

"""
apple
watermelon
"""
```
- key를 인자로 전달할 수 있음, key는 iterable 객체를 비교하는 기준이 정의된 함수 함수대신 lamdba 표현식도 전달이 가능.
- min(iterable, key)
```python
square = {2: 4, 3: 9, -1: 1, -2: 4}

key1 = min(square)
print(key1)

key2 = min(square, key = lambda k: square[k])
print(key2)

"""
-2
-1
"""
```
- 문자열 길이를 기준으로 최소, 최대값 찾기
```python
fruits = ['watermelon', 'kiwi', 'blueberry', 'apple']

print(min(fruits, key = lambda s: len(s)))
print(max(fruits, key = lambda s: len(s)))

"""
kiwi
watermelon
"""
```
