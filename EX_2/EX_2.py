n = int(input('число кустов: '))
qw = list(map(int, (input('Заполните список.Цифры вводить через ",": ').split(','))))
x = 0
for i in range(0, n-1):
    x = max(x,qw[i]+qw[i+1]+qw[i-1])
print(x)