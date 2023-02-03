def clean_text(string):
    string = string.replace(" ", "")
    string = string.replace(",", "")
    string = string.replace(".", "")
    string = string.replace("!", "")
    return string

def vigenere_cip(text, key, mode):
    result = ""
    key_index = 0
    text = clean_text(text)
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - 65
            if mode == "encrypt":
                result += chr((ord(char.upper()) - 65 + shift) % 26 + 65).lower() if char.islower() else chr((ord(char) - 65 + shift) % 26 + 65)
            elif mode == "decrypt":
                result += chr((ord(char.upper()) - 65 - shift) % 26 + 65).lower() if char.islower() else chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

def extended_vigenere(text, key, mode):
    result = ""
    key_index = 0
    text = clean_text(text)
    for char in text:
        char_code = ord(char)
        key_code = ord(key[key_index % len(key)])
        if mode == "encrypt":
            result += chr((char_code + key_code) % 256)
        elif mode == "decrypt":
            result += chr((char_code - key_code + 256) % 256)
        key_index += 1
    return result

# varian vigenere cipher (auto-key vigenere cipher)
def autokey_vigenere(text, key, mode):
    text = clean_text(text)
    if (mode == "encrypt" and len(key) < len(text)):
         key = key + text
         key = key[0:len(text)]
    return vigenere_cip(text, key, mode)

# affine cipher
def affine_cipher(text, m, b, mode):
    ALPHABET_SIZE = 26
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    
    result = ""
    
    for char in text:
        char_index = ALPHABET.find(char.lower())
        if char_index == -1:
            result += char
            continue
        if mode == "encrypt":
            shifted_index = (m * char_index + b) % ALPHABET_SIZE
            result += ALPHABET[shifted_index]
        elif mode == "decrypt":
            a_inv = 0
            for i in range(ALPHABET_SIZE):
                if (m * i) % ALPHABET_SIZE == 1:
                    a_inv = i
                    break
            shifted_index = (a_inv * (char_index - b + ALPHABET_SIZE)) % ALPHABET_SIZE
            result += ALPHABET[shifted_index]       
    return result

# hill cipher
def hill_cipher(text, key, mode):
    ALPHABET_SIZE = 26
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    
    result = ""
    key_matrix = [[int(i) for i in row.split()] for row in key.split("\n")]
    key_dimension = len(key_matrix)
    
    text = text.lower()
    text = [ALPHABET.find(char) for char in text if char in ALPHABET]
    
    if mode == "encrypt":
         for i in range(0, len(text), key_dimension):
            text_block = text[i:i + key_dimension]
            if len(text_block) < key_dimension:
                text_block += [0] * (key_dimension - len(text_block))
            ciphertext_block = [0] * key_dimension
            for j in range(key_dimension):
                for k in range(key_dimension):
                    ciphertext_block[j] += (key_matrix[j][k] * text_block[k]) % ALPHABET_SIZE
            result += "".join(ALPHABET[char % ALPHABET_SIZE] for char in ciphertext_block)
    elif mode == "decrypt":
        result = "can't decrypt"
    return result

def encrypt_playfair(key, plaintext):
    
    key = key.upper()
    plaintext = plaintext.upper()
    # prepare the matrix
    key = key.replace("J","I")
    
    plaintext = plaintext.replace("J","I")
    matrix = playfair_matrix(key)
    
    # format the plaintext
    if len(plaintext)%2==1:
        plaintext+='Z'
    # initialize the ciphertext
    ciphertext = ""
    # print(matrix)
    # loop through the plaintext by pairs
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        # print(a)
        # get the position of each character in the matrix
        a_row, a_col = get_position(matrix, a)
        b_row, b_col = get_position(matrix, b)
        
        # apply the rule for encryption
        if a_row == b_row:
            # same row
            ciphertext += matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
        elif a_col == b_col:
            # same column
            ciphertext += matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
        else:
            # different row and column
            ciphertext += matrix[a_row][b_col] + matrix[b_row][a_col]
        print(i, a,b, ciphertext)
    
    return ciphertext

def decrypt_playfair(key, ciphertext):
    # prepare the matrix
    
    key = key.upper()
    ciphertext = ciphertext.upper()
    key = key.replace("J","I")
    
    ciphertext = ciphertext.replace("J","I")
    matrix = playfair_matrix(key)
    
    # initialize the plaintext
    plaintext = ""
    # loop through the ciphertext by pairs
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        
        # get the position of each character in the matrix
        a_row, a_col = get_position(matrix, a)
        b_row, b_col = get_position(matrix, b)
        
        # apply the rule for decryption
        if a_row == b_row:
            # same row
            plaintext += matrix[a_row][(a_col - 1) % 5] + matrix[b_row][(b_col - 1) % 5]
        elif a_col == b_col:
            # same column
            plaintext += matrix[(a_row - 1) % 5][a_col] + matrix[(b_row - 1) % 5][b_col]
        else:
            # different row and column
            plaintext += matrix[a_row][b_col] + matrix[b_row][a_col]
    
    return plaintext


def generate_matrix(key):
    key = key.replace(" ", "").upper()
    matrix = []
    for char in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in matrix:
            matrix.append(char)
    return matrix

def playfair_matrix(key):
    matrix = generate_matrix(key)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def get_position(matrix, char):
    # print(matrix)
    for i in range(5):
        for j in range(5):
            # print(matrix[i][j], "==", char)
            if matrix[i][j] == char:
                # print(i,j)
                return (i, j)
    return None
