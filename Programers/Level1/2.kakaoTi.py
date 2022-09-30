survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

number = [0,3,2,1]
for i in range(len(survey)):
    if 1 <= choices[i] < 4:
        dic[survey[i][0]] += number[choices[i]]
    elif 4 < choices[i] <= 7:
        dic[survey[i][1]] += choices[i] - 4

result = ''
if dic['R'] >= dic['T']:
    result += 'R'
else :
    result += 'T'
if dic['C'] >= dic['F']:
    result += 'C'
else :
    result += 'F'
if dic['J'] >= dic['M']:
    result += 'J'
else :
    result += 'M'
if dic['A'] >= dic['N']:
    result += 'A'
else :
    result += 'N'
print(result)