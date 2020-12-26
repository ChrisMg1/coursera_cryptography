import sys
import binascii
from week1_OTP import XORspecificHEXinput

def printStringLength(in_str):
    return len(in_str.encode('utf-8'))

def printByteLength(in_str):
    return sys.getsizeof(in_str)

def HEXtoINT(in_hex):
    return int(in_hex, 16)


msg1 = 'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.'
msg2 = 'The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.'
msg3 = 'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.'
msg4 = 'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.'

msg5 = 'test'

allMSG = [msg1, msg2, msg3, msg4]#, msg5]


for i in allMSG:
    print(i[:8], '; String: ', printStringLength(i))
    print(i[:8], '; Byte: ', printByteLength(i) % 16)


hex_out10 = '9f970f4e932330e4'
hex_out11 = '6068f0b1b645c008'

hex_out20 = '7c2822ebfdc48bfb'
hex_out21 = '325032a9c5e2364b'

hex_out30 = '4af532671351e2e1'
hex_out31 = '87a40cfa8dd39154'

hex_out40 = '2d1cfa42c0b1d266'
hex_out41 = 'eea6e3ddb2146dd0'

long_list = [hex_out10, hex_out11, hex_out20, hex_out21, hex_out30, hex_out31, hex_out40, hex_out41]
###################################

hex_out101 = '9f970f4e'
hex_out102 = '932330e4'
hex_out111 = '6068f0b1'
hex_out112 = 'b645c008'

hex_out201 = '7c2822eb'
hex_out202 = 'fdc48bfb'
hex_out211 = '325032a9'
hex_out212 = 'c5e2364b'

hex_out301 = '4af53267'
hex_out302 = '1351e2e1'
hex_out311 = '87a40cfa'
hex_out312 = '8dd39154'

hex_out401 = '2d1cfa42'
hex_out402 = 'c0b1d266'
hex_out411 = 'eea6e3dd'
hex_out412 = 'b2146dd0'


out_list = [hex_out101, hex_out102, hex_out111, hex_out112, hex_out201, hex_out202, hex_out211, hex_out212,
            hex_out301, hex_out302, hex_out311, hex_out312, hex_out401, hex_out402, hex_out411, hex_out412]

print(out_list)

test_hex = 'ff'
#print(len(out_list))

rel_list = []

print('---start loop---')

for j in range(len(out_list)):
    if j % 2:
        calc = HEXtoINT(out_list[j]) / HEXtoINT(out_list[j-1])

        print(j, '\n', calc)

        rel_list.append(calc)

        bin1 = binascii.a2b_hex(out_list[j])
        bin2 = binascii.a2b_hex(out_list[j - 1])

        myXORed = bytes(a ^ b for (a, b) in zip(bin1, bin2))

        # print(myXORed)


        # print(out_list[j])

for k in range(len(long_list)):
    if k % 2:
        # print(rel_list[k] / rel_list[k-1])

        print(XORspecificHEXinput(long_list[k], long_list[k-1]), long_list[k][:8])

# print(rel_list)