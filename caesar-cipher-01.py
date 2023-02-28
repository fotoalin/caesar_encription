# Author: Alin Morosanu
# Date: 2023-02-28
# Description: encript and decript strings using Ceasar cipher method

alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numb = '0123456789'
punc = '.,?!:;'

def encrypt(message, key):
    result = ''
    for char in message:
        if char in alpha_lower:
            result += alpha_lower[(alpha_lower.find(char) + key) % 26]
        elif char in alpha_upper:
            result += alpha_upper[(alpha_upper.find(char) + key) % 26]
        elif char in numb:
            result += numb[(numb.find(char) + key) % 10]
        elif char in punc:
            result += punc[(punc.find(char) + key) % 7]
        else:
            result += char
    
    return result



def decrypt(message, key):
    result = ''
    for char in message:
        if char in alpha_lower:
            result += alpha_lower[(alpha_lower.find(char) - key) % 26]
        elif char in alpha_upper:
            result += alpha_upper[(alpha_upper.find(char) - key) % 26]
        elif char in numb:
            result += numb[(numb.find(char) - key) % 10]
        elif char in punc:
            result += punc[(punc.find(char) - key) % 7]
        else:
            result += char
    
    return result




def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)
    
    print("Encrypted message: ", encrypted_message)
    print("Decrypted message: ", decrypted_message)

if __name__ == '__main__':
    main()
