n = int(input())
m = int(input())


arr = [i + 1 for i in range(n)]
cur = 1
num = m # порядковый номер элемента в циклическом массиве
ind = num % n - 1 # соответствующий ИНДЕКС порядковому номеру
next = arr[ind]
print(cur, end='')

while next != 1:
    cur = next
    print(cur, end='')
    num += m - 1
    ind = num % n - 1 
    next = arr[ind]