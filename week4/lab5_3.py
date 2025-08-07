def encode_char(char, rotor_position):
    if rotor_position <=0:
        return 0/0
    ascii = ord(char)
    n = 0
    if rotor_position%26 == 0:
        rotor_position+=1
        
    if ascii < ord('A') or ascii>ord('z') or (ascii > ord("Z") and ascii<ord('a')):
        return char,0
    rotate = rotor_position % 26
    ascii = ascii+rotate
    if ascii >= 97+26:
        ascii = ord('a')-1+((ascii-ord('z'))%26)
    elif ascii > (ord('Z')) and ord(char) < ord('a'):
        ascii = ord('A')-1 + ((ascii-ord('Z'))%26)
    char = chr(ascii)
    
    return char,n
    #coding here

def decode_char(char, rotor_position):
    if rotor_position <=0:
        return 0/0
    n=0
    ascii = ord(char)
    rotate = rotor_position%26
    
    if rotate == 0:
        rotate = 1
        n=0
    if ascii < ord('A') or ascii>ord('z') or (ascii > ord("Z") and ascii<ord('a')):
        return char,0
    elif ascii >=ord('a'):
        ascii -= rotate
        if ascii < ord('a'):
            ascii = ord('z')-rotate+1-ord('a')+ord(char)
    elif ascii >= ord('A') and ascii <=ord('Z'):
        ascii -= rotate
        
        if ascii < ord('A'):
            
            ascii = ord('Z')-rotate+1-ord('A')+ord(char)
            
            
    char = chr(ascii)
    
    # print(char,end=" ")
    return char,n
    #coding here

def encode_message(message, rotor_position,encode = [],n=1):
    #coding here
    out = encode
    message = list(message)
    message.append
    if len(message) == 0:
        return out
    char,temp_n = encode_char(message.pop(0),rotor_position+(n-1))
    n+=1
    n+=temp_n
    out.append(char)
    message = "".join(message)
    return "".join(encode_message(message, rotor_position,out,n))

def decode_message(encoded_message, rotor_position,n=1,decode =[]):
    out = decode
    
    encoded_message = list(encoded_message)
    if len(encoded_message) == 0:
        return out
    char,n_1 = decode_char(encoded_message.pop(0),rotor_position+(n-1))
    n+=1
    n+=n_1
    # print(n)
    out.append(char)
    # print(out)
    encoded_message = "".join(encoded_message)
    return "".join(decode_message(encoded_message, rotor_position,n,out))
    pass
    

# การใช้งาน
print("This is Caesar cipher")
message ,initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:",encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)