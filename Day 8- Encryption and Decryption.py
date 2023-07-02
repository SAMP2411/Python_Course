# 97 - 122 are the ascii codes for small a-z
# ord("any_alphabet") will give its ascii value in int
# chr(any_number) will give its character value in string
# print(f"\nThe word is : {''.join(blank_list)}")

logo = (
    """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""
    """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP"""
    """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
)

print(logo)
flag = True
num_list = []


def encode_decode(n):
    for items in word_list:
        if ord(items) > 122 or ord(items) < 97:
            num_list.append(items)
        else:
            newItem = ord(items) + (n * userShift)
            if not newItem > 122 and not newItem < 97:
                num_list.append(chr(newItem))
            elif newItem > 122:
                num_list.append(chr(newItem - 26))
            else:
                num_list.append(chr(newItem + 26))

    return num_list


while flag:
    encrypt_decrypt = input("Type 'encode' to encrypt, 'decode' to decrypt : \n")

    if encrypt_decrypt == "encode":
        eOrD = 1
    elif encrypt_decrypt == "decode":
        eOrD = -1
    else:
        print("Invalid response !!")
        break

    num_list = []
    userInput = input("\nType your message : ").lower()
    # print(userInput)
    userShift = int(input("Type the shift number : "))

    word_list = []
    word_list[:] = userInput
    # print(word_list)

    print(f"Here's the result : {''.join(encode_decode(eOrD))}\n")
    move_further = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if move_further == "no":
        flag = False
