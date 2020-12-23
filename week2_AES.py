from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad





print('DECODING')

def cbc_decrypt(my_key, my_ct, pad):
    cipher = AES.new(bytes.fromhex(my_key), AES.MODE_CBC, iv=bytes.fromhex(my_ct[ 0 : 32 ]))
    plain = cipher.decrypt(bytes.fromhex(my_ct))
    plain = unpad(plain, pad)
    return plain

def ctr_decrypt(my_key, my_ct):
    cipher = AES.new(bytes.fromhex(my_key), AES.MODE_CTR, nonce = bytes.fromhex(my_ct[ 0 : 16 ]))
    plain = cipher.decrypt(bytes.fromhex(my_ct))
    #plain = unpad(plain, 8)
    return plain

print(cbc_decrypt('140b41b22a29beb4061bda66b6747e14', '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81', 8))
print(cbc_decrypt('140b41b22a29beb4061bda66b6747e14', '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253', 16))
#print(ctr_decrypt('36f18357be4dbd77f050515c73fcf9f2', '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'))


#plain = unpad(plain, 8)#

# print(plain.decode())