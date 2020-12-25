
def printByteLength(in_str):
    return len(in_str.encode('utf-8'))

msg1 = 'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.'
msg2 = 'The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.'
msg3 = 'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.'
msg4 = 'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.'

allMSG = [msg1, msg2, msg3, msg4]


for i in allMSG:
    print(len(i.encode()))
    print(printByteLength(i))