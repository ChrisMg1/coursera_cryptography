print( (2**10001) % 11)

print( (2**245) % 35)

gen = 13
sta = 2

print('----- generators ------')

for i in range(0, 12):
    print( (sta**i) % gen)

print('---Z23---')

j = 1

while ((j**2) + 4*j + 1) % 23 != 0:
    j=j+1
print(j)