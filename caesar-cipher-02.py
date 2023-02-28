def caesar_encrypt(plaintext, shift):
    """Encrypts the plaintext message using the Caesar cipher method with the given shift.

        # ord(char.lower()) - 97 + shift - This expression converts the current character to its ASCII code using the ord() function, converts it to lowercase using the lower() method, subtracts 97 to shift it to the range of 0 to 25 (the ASCII codes for lowercase letters a to z start at 97), and adds the shift value to shift it by the desired number of positions. For example, if the character is "a" and the shift value is 3, this expression evaluates to 0+3=3 (the ASCII code for "d").
        # 
        # % 26 - This operator wraps the result of the previous expression around so that it falls within the range of 0 to 25, regardless of the value of the shift. For example, if the previous result was 26, this operator would wrap it around to 0.
        # 
        # + 97 - This operator adds 97 to the result of the previous expression to convert it back to the range of ASCII codes for lowercase letters. For example, if the previous result was 3, this operator would add 97 to get 100 (the ASCII code for "d").
        # 
        # chr(...) - This function call converts the result of the previous expression, which is an ASCII code, back to its corresponding character using the chr() function.
        # 
        # if char.islower() else ... - This is a ternary conditional operator that checks whether the current character in the plaintext is lowercase. If it is, the expression before the else keyword is evaluated; otherwise, the expression after the else keyword is evaluated.
        # 
        # chr((ord(char.upper()) - 65 + shift) % 26 + 65) - This expression is evaluated if the current character in the plaintext is uppercase. It works similarly to the expression for lowercase characters, but uses the ASCII codes for uppercase letters instead (which start at 65). Specifically, it converts the current character to its ASCII code using the ord() function, converts it to uppercase using the upper() method, subtracts 65 to shift it to the range of 0 to 25 (the ASCII codes for uppercase letters A to Z start at 65), adds the shift value to shift it by the desired number of positions, wraps the result around to the range of 0 to 25 using % 26, adds 65 to convert it back to the range of ASCII codes for uppercase letters, and finally converts the result back to a character using the chr() function.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Convert the character to its ASCII code, shift it, and convert it back to a character
            # while preserving its case (uppercase/lowercase)
            ciphertext += chr((ord(char.lower()) - 97 + shift) % 26 + 97) if char.islower() else chr((ord(char.upper()) - 65 + shift) % 26 + 65)
        else:
            # Non-alphabetic characters are left unchanged
            ciphertext += char
    return ciphertext





def caesar_decrypt(ciphertext, shift):
    """Decrypts the ciphertext message using the Caesar cipher method with the given shift.
    
        # ord(char.lower()) - 97 - shift - This expression converts the current character to its ASCII code using the ord() function, converts it to lowercase using the lower() method, subtracts 97 to shift it back to the range of 0 to 25 (the ASCII codes for lowercase letters a to z start at 97), and subtracts the shift value to undo the previous shift operation. For example, if the character is "d" and the shift value is 3, this expression evaluates to 3 (the ASCII code for "a").
        # 
        # % 26 - This operator wraps the result of the previous expression around so that it falls within the range of 0 to 25, regardless of the value of the shift. For example, if the previous result was -1, this operator would wrap it around to 25.
        # 
        # + 97 - This operator adds 97 to the result of the previous expression to convert it back to the range of ASCII codes for lowercase letters. For example, if the previous result was 3, this operator would add 97 to get 100 (the ASCII code for "d").
        # 
        # chr(...) - This function call converts the result of the previous expression, which is an ASCII code, back to its corresponding character using the chr() function.
        # 
        # if char.islower() else ... - This is a ternary conditional operator that checks whether the current character in the ciphertext is lowercase. If it is, the expression before the else keyword is evaluated; otherwise, the expression after the else keyword is evaluated.
        # 
        # chr((ord(char.upper()) - 65 - shift) % 26 + 65) - This expression is evaluated if the current character in the ciphertext is uppercase. It works similarly to the expression for lowercase characters, but uses the ASCII codes for uppercase letters instead (which start at 65). Specifically, it converts the current character to its ASCII code using the ord() function, converts it to uppercase using the upper() method, subtracts 65 to shift it back to the range of 0 to 25 (the ASCII codes for uppercase letters A to Z start at 65), subtracts the shift value to undo the previous shift operation, wraps the result around to the range of 0 to 25 using % 26, adds 65 to convert it back to the range of ASCII codes for uppercase letters, and finally converts the result back to a character using the chr() function.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Convert the character to its ASCII code, shift it back, and convert it back to a character
            # while preserving its case (uppercase/lowercase)
            plaintext += chr((ord(char.lower()) - 97 - shift) % 26 + 97) if char.islower() else chr((ord(char.upper()) - 65 - shift) % 26 + 65)
        else:
            # Non-alphabetic characters are left unchanged
            plaintext += char
    return plaintext
