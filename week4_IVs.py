from week1_OTP import XORspecificHEXinput, STRINGtoHEX

IV = '20814804c1767293b99f1d9cab3bc3e7'
ct = 'ac1e37bfb15599e5f40eef805488281d'
pt = 'Pay Bob 100$'

hex_1 = STRINGtoHEX('1')
hex_5 = STRINGtoHEX('5')


print(len(IV), len(ct), len(pt))

firstXOR = XORspecificHEXinput('b9', hex_1)
secondXOR = XORspecificHEXinput(firstXOR, hex_5)

print('out: ', secondXOR)

# print(hex_5)
