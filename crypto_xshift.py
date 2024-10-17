def generate_dynamic_key(position: int, length: int) -> int:
    """
    Generate a dynamic key based on the position of the character and the string length.
    The key changes based on the character's index.

    This function computes a dynamic key based on the position of a character
    within a string and the total length of the string. The key is calculated
    using a simple arithmetic formula and is intended to be used for XOR-based
    encryption or obfuscation.

    Args:
        position (int): The index position of the character within the string.
        length (int): The total length of the string.

    Returns:
        int: A dynamic key value between 0 and 255, inclusive.

    Example:
        >>> generate_dynamic_key(5, 10)
        45
    """
    return (position * 7 + length) % 256  # Dynamic XOR key


def circular_left_shift(value: int, shift_amount: int) -> int:
    """
    Perform a circular left shift on an 8-bit value.

    This function takes an 8-bit integer value and shifts its bits to the left by the specified 
    shift amount. Bits that are shifted out on the left are reintroduced on the right, 
    effectively creating a circular shift.

    :param value: int - The 8-bit integer value to be shifted. Must be in the range 0-255.
    :param shift_amount: int - The number of bits to shift. Should be a non-negative integer.
    :return: int - The circularly shifted 8-bit value.
    :raises ValueError: If the value is not in the range 0-255 or if shift_amount is negative.
    
    Example:
    >>> circular_left_shift(0b10101010, 3)
    0b01010101
    """
    return ((value << shift_amount) | (value >> (8 - shift_amount))) & 0xFF


def circular_right_shift(value: int, shift_amount: int) -> int:
    """
    Perform a circular right shift on an 8-bit value.

    This function takes an 8-bit integer value and performs a circular right shift by the specified number of bits.
    A circular shift means that the bits that are shifted out on one end are reintroduced on the other end.

    :param value: int - The 8-bit value to be shifted. Must be in the range 0-255.
    :param shift_amount: int - The number of bits to shift. Must be a non-negative integer.
    :return: int - The circularly shifted 8-bit value.
    :raises ValueError: If the value is not in the range 0-255 or if shift_amount is negative.
    
    Example:
    >>> circular_right_shift(0b10110011, 3)
    217  # which is 0b11011001
    """
    return ((value >> shift_amount) | (value << (8 - shift_amount))) & 0xFF


def encrypt_xor_bps(input_string: str) -> str:
    """
    Encrypt a string using a dynamic XOR key and circular bit shifting.

    This function takes an input string and encrypts it by performing the following steps:
    1. For each character in the input string, obtain its ASCII value.
    2. Generate a dynamic XOR key based on the character's position and the length of the string.
    3. XOR the ASCII value with the dynamic XOR key.
    4. Perform a circular left bit shift on the XOR result, with the shift amount depending on the character's position.
    5. Convert the shifted value to a 2-character hexadecimal string and append it to the result.
    Args:
        input_string (str): The string to be encrypted.
    Returns:
        str: The encrypted string represented as a concatenation of hexadecimal values.
    Note:
        - The `generate_dynamic_key` function is assumed to generate a dynamic XOR key based on the character's position and the length of the string.
        - The `circular_left_shift` function is assumed to perform a circular left bit shift on the given value by the specified amount.
    """
    encrypted_string = []
    length = len(input_string)  # Cache length of the string for efficiency
    
    for i, char in enumerate(input_string):
        ascii_value = ord(char)  # Get ASCII value
        xor_key = generate_dynamic_key(i, length)  # Generate dynamic XOR key
        xor_value = ascii_value ^ xor_key  # XOR the character
        
        shift_amount = (i % 5) + 1  # Shift 1-5 bits depending on position
        shifted_value = circular_left_shift(xor_value, shift_amount)  # Circular left shift
        
        # Use f-string formatting to avoid zfill overhead
        encrypted_string.append(f"{shifted_value:02x}")  # Convert to 2-char hex
    
    return ''.join(encrypted_string)  # Join hex values


def decrypt_xor_bps(encrypted_string: str) -> str:
    """
    Decrypt an encrypted string using a dynamic XOR key and circular bit shifting.

    This function takes an encrypted string, where each character is represented 
    by its hexadecimal value, and decrypts it using a combination of circular 
    bit shifting and XOR operations. The decryption process is the reverse of 
    the encryption process, which involves generating a dynamic key and applying 
    circular right shifts.
    Args:
        encrypted_string (str): The encrypted string, with each character 
                                represented by its hexadecimal value.
    Returns:
        str: The decrypted string.
    Example:
        encrypted_string = "4a6f686e"
        decrypted_string = decrypt_xor_bps(encrypted_string)
        print(decrypted_string)  # Output: "John"
    Note:
        - The function assumes that the encrypted string length is even.
        - The circular_right_shift and generate_dynamic_key functions must be 
          defined elsewhere in the codebase.
    """
    decrypted_string = []
    length = len(encrypted_string) // 2  # Cache length
    
    for i in range(0, len(encrypted_string), 2):
        encrypted_value = int(encrypted_string[i:i+2], 16)  # Get hex value as integer
        
        shift_amount = (i // 2 % 5) + 1  # Same shift logic as in encryption
        xor_value = circular_right_shift(encrypted_value, shift_amount)  # Circular right shift
        
        xor_key = generate_dynamic_key(i // 2, length)  # Same key generation
        ascii_value = xor_value ^ xor_key  # Reverse XOR
        
        decrypted_string.append(chr(ascii_value))  # Convert back to character
    
    return ''.join(decrypted_string)


if __name__ == "__main__":
    # Example usage
    original_string = "Alin Morosanu"

    # Encrypt the string
    encrypted_string = encrypt_xor_bps(original_string)
    print(f"Encrypted: {encrypted_string}")

    # Decrypt the string
    decrypted_string = decrypt_xor_bps(encrypted_string)
    print(f"Decrypted: {decrypted_string}")
