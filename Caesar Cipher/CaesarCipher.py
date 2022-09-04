# Caesar Cipher ASCII Art

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


print(f"Welcome to the\n{logo}")
loop = 'yes'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(text, shift):
    result = ''
    for i in text:
        # for all symbols, numbers and spaces
        if i not in alphabet:
            result += i 
        else:
            # % 26 so we don't get IndexError: Index out of range
            result += alphabet[(alphabet.index(i) + shift) % 26]
    return result

def decode(text, shift):
    result = ''
    for i in text:
        # for all symbols, numbers and spaces
        if i == ' ':
            result += i 
        else:

            result += alphabet[alphabet.index(i) - shift]
    return result

while loop == 'yes':
    user_input = input("Type 'encode' for encoding a message, and type 'decode' for decoding a message.\n").lower()
    shift = int(input("By how many letters do you want to shift it to.\n"))
    shift = shift % 26
    text = input("Type the message.\n").lower()

    if user_input == 'encode':
        print(encode(text, shift))
    elif user_input == 'decode':
        print(decode(text, shift))
    loop = input("Type 'yes' if you want to do it again, or type 'no' if you want to exit.\n").lower()

    if loop == 'no':
        print("Goodbye!")
        break
