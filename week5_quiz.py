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

print('----#5:Z23----')
a = 1
b = 1

while ((7 * a) + (23 * b)) % 23 != 1:
    print(a, b)
    b=b+1
    if b>100*a:
        a=a+1
        b=1

print(a, b)
print(((7 * a) + (23 * b)) % 23)

print('---inverse---')
c=1
while (7 * c) % 23 !=1:
    c=c+1
print(c)
print((10*7)%23)

print('-----gcd_Z35----')

from math import gcd

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount#

print(phi(35))

print('----#10_order-2-----')

a=1
while (2**a) % 35 != 1:
    a=a+1
print(a)
print(2**a)
print(2**a % 35)

print('-----#13:11th root -----')
x=0

while (x**11) % 19 != 2:
    x=x+1
print(x)

print('----#14 discrete log----')
y=1
while (2**y) % 13 != 5:
    y=y+1

print(y)

print((2**9) % 13)
