from hashlib import sha256

# file_path = 'C:/Users/ZVM_XSP15_03/Downloads/6.2.birthday.mp4_download'
# file_path = 'C:/Users/blue/Downloads/6.2.birthday.mp4_download'

file_path = 'C:/Users/ZVM_XSP15_03/Downloads/6.1.intro.mp4_download'

aim_output = '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8'

block_length = 1024

byte_counter = 1

first_bytes = bytearray(b'')

print(first_bytes)

list_byte_h0 = []

with open(file_path, "rb") as f:
    while (byte := f.read(1)):
        # Do stuff with byte.
        # print(len(list_byte_h0), ' : ', byte, type(byte), byte[0], type(byte[0]), len(list_byte_h0) * 1024)
        first_bytes.append(byte[0])
        if byte_counter % block_length == 0:
            list_byte_h0.append(bytes(first_bytes))
            first_bytes = bytearray(b'')
        byte_counter = byte_counter + 1

    list_byte_h0.append(bytes(first_bytes))

print(first_bytes, type(first_bytes))



first_bytes = bytes(first_bytes)

# print('bytearray(', first_bytes, type(first_bytes), sep='')

print(first_bytes, type(first_bytes), len(first_bytes))


print(len(list_byte_h0))
aux = b''
for i in reversed(list_byte_h0):
    h2 = sha256()
    h2.update(i + aux)
    aux = h2.digest()

print(h2.hexdigest())
print(h2.hexdigest() == aim_output)
