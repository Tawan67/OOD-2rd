print(ord('a')-ord('Z'))
# upper = [chr(i) for i in range(65,91,1)]
# lower = [chr(i) for i in range(97,123,1)]
# print(upper)
# print(lower)

def encode_char(char, rotor_position):
    upper = [chr(i) for i in range(65,91,1)]
    lower = [chr(i) for i in range(97,123,1)]
    ascii = ord(char)
    
    if rotor_position%26 == 0:
        rotor_position+=1
    rotate = rotor_position%26
    if char in upper:
        current = upper.index(char)
        rotate += current
        char = upper[rotate]
        return char
print(encode_char("A",25))