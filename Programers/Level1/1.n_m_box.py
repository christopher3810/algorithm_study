n, m = map(int, input().strip().split(' '))

# 5 3
list = []
for i in range (m):
    string = ''
    for j in range (n):
        string += "*"
    list.append(string)
for i in list:
    print(i)