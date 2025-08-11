def encode_char(char, rotor_position):
    
    
    upper = [chr(i) for i in range(65,91,1)]
    lower = [chr(i) for i in range(97,123,1)]
    n = 0
    if rotor_position%26 == 0:
        rotor_position+=1
        n = 1
    rotate = rotor_position%26
    if char in upper:
        current = upper.index(char)
        rotate += current
        rotate = rotate%26
        char = upper[rotate]
        return char,n
    elif char in lower:
        current = lower.index(char)
        rotate += current
        rotate = rotate%26
        char = lower[rotate]
        return char,n
    return char,0
    #coding here

def decode_char(char, rotor_position):
    
    upper = [chr(i) for i in range(65,91,1)]
    lower = [chr(i) for i in range(97,123,1)]
    n = 0
    if rotor_position%26 == 0:
        rotor_position+=1
        n = 1
        
    rotate = rotor_position%26
    
    if char in upper:
        current = upper.index(char)
        current -= rotate
        if current < 0:
            current = 26+current
        char = upper[current]
        return char,n
    elif char in lower:
        current = lower.index(char)
        current -= rotate
        if current < 0:
            current = 26+current
        char = lower[current]
        return char,n
    return char,0
 

def encode_message(message, rotor_position,encode = [],n=1):
    if rotor_position == 0:
        return message
    #coding here
    out = encode
    message = list(message)
    message.append
    if len(message) == 0:
        return out
    char,t= encode_char(message.pop(0),rotor_position+(n-1))
    n+=1
    n+=t
    out.append(char)
    message = "".join(message)
    return "".join(encode_message(message, rotor_position,out,n))

def decode_message(encoded_message, rotor_position,n=1,decode =[]):
    if rotor_position == 0:
        return encoded_message
    out = decode
    
    encoded_message = list(encoded_message)
    if len(encoded_message) == 0:
        return out
    char,t = decode_char(encoded_message.pop(0),rotor_position+(n-1))
    n+=1
    n+=t
    out.append(char)
    encoded_message = "".join(encoded_message)
    return "".join(decode_message(encoded_message, rotor_position,n,out))

    

# การใช้งาน
print("This is Caesar cipher")
message ,initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:",encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)