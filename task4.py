with open('input.txt', 'r') as f:
    str_file = f.read()
    arr = list(map(int, str_file.split()))

avg = sum(arr) // len(arr)
result = sum([abs(avg - i) for i in arr])
print(result)