f1 = open('файл1.txt', 'r')
input1 = f1.read().split()
a = float(input1[0])
b = float(input1[1])
r = float(input1[2])
f1.close()

with open('файл2.txt', 'r') as f2:
    lines = f2.readlines()
    for line in lines:
        x, y = [float(p) for p in line.split()]
        right = r**2
        left = (x - a)**2 + (y - b)**2
        if right == left:
            print(0)
        elif right > left:
            print(1)
        elif right < left:
            print(2)