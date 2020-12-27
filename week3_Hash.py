from hashlib import sha256

# file_path = 'C:/Users/ZVM_XSP15_03/Downloads/6.2.birthday.mp4_download'

file_path = 'C:/Users/blue/Downloads/6.2.birthday.mp4_download'

aim_output = '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8'

length_in_byte = 32

act_length = 0

first_bytes = bytearray(b'')

print(first_bytes)

with open(file_path, "rb") as f:
    while (byte := f.read(1)) and act_length < length_in_byte:
        pass
        # Do stuff with byte.
        print(act_length, ' : ', byte, type(byte), byte[0], type(byte[0]))
        first_bytes.append(byte[0])
        act_length = act_length + 1

print(first_bytes, type(first_bytes))



first_bytes = bytes(first_bytes)

# print('bytearray(', first_bytes, type(first_bytes), sep='')

print(first_bytes, type(first_bytes), len(first_bytes))

h = sha256()
h.update(first_bytes)
aux = h.digest()

print('aux: ', aux.hex(), type(aux.hex()))

print(aux.hex() == aim_output)