
file_path = 'C:/Users/ZVM_XSP15_03/Downloads/6.2.birthday.mp4_download'

aim_output = '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8'

length_in_byte = 32

act_length = 0

with open(file_path, "rb") as f:
    while (byte := f.read(1)) and act_length < length_in_byte:
        pass
        # Do stuff with byte.
        print(act_length, ' : ', byte)
        act_length = act_length + 1


print(file_path == aim_output)