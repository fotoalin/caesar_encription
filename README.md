# Caesar Cipher Python Function v02

This repository contains two Python functions that can be used to encrypt and decrypt messages using the Caesar cipher method.

The Caesar cipher is a simple substitution cipher that shifts each letter of the message a certain number of positions to the right or left in the alphabet. For example, if the shift value is 3, the letter "a" would be replaced by the letter "d", "b" would be replaced by "e", and so on.

## Functions
`caesar_encrypt(plaintext, shift)`

Encrypts the plaintext message using the Caesar cipher method with the given shift.

### Arguments

    `plaintext`: The plaintext message to be encrypted. Must be a string.
    `shift`: The shift value used to encrypt the message. Must be an integer.

### Returns

    The encrypted ciphertext message, as a string.

`caesar_decrypt(ciphertext, shift)`

Decrypts the ciphertext message using the Caesar cipher method with the given shift.

### Arguments

    `ciphertext`: The ciphertext message to be decrypted. Must be a string.
    `shift`: The shift value used to encrypt the message. Must be an integer.

### Returns

    The decrypted plaintext message, as a string.
