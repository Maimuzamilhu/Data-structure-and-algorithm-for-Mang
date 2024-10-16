import numpy as np


# Step 1: Custom letter-to-number mapping (Z=0, A=25)
def letter_to_num(letter):
    # Mapping Z = 0, A = 25
    return (ord(letter) - ord('A') + 1) % 26 if letter != 'Z' else 0


def num_to_letter(num):
    # Reverse the mapping where Z = 0, A = 25
    return 'Z' if num == 0 else chr((num - 1) + ord('A'))


# Step 2: Convert text into matrix of numbers using the custom mapping
def text_to_matrix(text):
    numbers = [letter_to_num(char) for char in text]
    return np.array(numbers).reshape(-1, 3)


# Step 3: Hill cipher encryption process with matrix multiplication and mod 26
def hill_cipher_encrypt(plain_text, key_matrix):
    # Filter plain text (remove spaces and make uppercase)
    plain_text = ''.join(plain_text.upper().split())

    # Padding if plain text length is not divisible by 3
    while len(plain_text) % 3 != 0:
        plain_text += 'Z'  # Add 'Z' as padding

    # Convert plain text to matrix form (each 3 letters)
    plain_text_matrix = text_to_matrix(plain_text)

    # Initialize empty list for storing cipher text
    cipher_text = []

    # Perform matrix multiplication and mod 26 for each block
    for block in plain_text_matrix:
        # Perform custom matrix multiplication according to the provided formula
        c1 = (block[0] * key_matrix[0, 0] + block[1] * key_matrix[1, 0] + block[2] * key_matrix[2, 0]) % 26
        c2 = (block[0] * key_matrix[0, 1] + block[1] * key_matrix[1, 1] + block[2] * key_matrix[2, 1]) % 26
        c3 = (block[0] * key_matrix[0, 2] + block[1] * key_matrix[1, 2] + block[2] * key_matrix[2, 2]) % 26

        # Append the results to the cipher text list
        cipher_text.extend([num_to_letter(c1), num_to_letter(c2), num_to_letter(c3)])

    return ''.join(cipher_text)


# Step 4: Define the key matrix (as provided)
key_matrix = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

# Example plain text (as provided)
plain_text = "you people are studing in AI"

# Encrypt the plain text using the Hill cipher
cipher_text = hill_cipher_encrypt(plain_text, key_matrix)

print("\nFinal Cipher Text:", cipher_text)
