import sys
import binascii
from week1_OTP import XORspecificHEXinput


def printStringLength(in_str):
    return len(in_str)


def printByteLength(in_str):
    return sys.getsizeof(in_str)


def HEXtoINT(in_hex):
    return int(in_hex, 16)


msg3 = 'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.'
msg1 = 'To consider the resistance of an enciphering process to being broken we should assume that at same times the enemy knows everything but the key being used and to break it needs only discover the key from this information.'
msg2 = 'We see immediately that one needs little information to begin to break down the process.'
msg4 = 'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.'

msg5 = 'test.'

allMSG = [msg1, msg2, msg3, msg4, msg5]


for i in allMSG:
    print(i[:8], '; String: ', printStringLength(i))

hex_out10 = 'e86d2de2e1387ae9'
hex_out11 = '1792d21db645c008'

hex_out20 = '5f67abaf5210722b'
hex_out21 = 'bbe033c00bc9330e'

hex_out30 = '7c2822ebfdc48bfb'
hex_out31 = '325032a9c5e2364b'

hex_out40 = '7b50baab07640c3d'
hex_out41 = 'ac343a22cea46d60'

long_list = [hex_out10, hex_out11, hex_out20, hex_out21, hex_out30, hex_out31, hex_out40, hex_out41]

for k in range(len(long_list)):
    if k % 2:
        print(XORspecificHEXinput(long_list[k], long_list[k-1]), long_list[k][:6])

print(112 % 16)

# padding: 16 byte
