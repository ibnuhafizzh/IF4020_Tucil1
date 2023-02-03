import numpy as np
def adjoint(A):
    # Check if matrix is square
    rows, cols = np.shape(A)
    if rows != cols:
        raise ValueError("Matrix is not square")

    # Find the adjoint matrix
    adjA = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            adjA[i][j] = (-1)**(i+j) * np.linalg.det(np.delete(np.delete(A, i, axis=0), j, axis=1))
    return np.transpose(adjA)

def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(n):
            sub_matrix = [[matrix[j][k] for k in range(n) if k != i] for j in range(1, n)]
            determinant += (-1)**i * matrix[0][i] * det(sub_matrix)
        return determinant

def determinant_mod(matrix):
    determinant = det(matrix)
    determinant = determinant%26
    return determinant
def inverse_modulo(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def modulo_inverse_mat(matrix, mod):
    adjoin_mat = adjoint(matrix)
    det_mod = determinant_mod(matrix)
    inverse_mod = inverse_modulo(det_mod,26)
    adjoin_mat = adjoin_mat*inverse_mod

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            adjoin_mat[i][j] = adjoin_mat[i][j]%mod
    return adjoin_mat

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
        key_inv = (np.round(modulo_inverse_mat(key_matrix, 26)).astype(np.int64).tolist())
        for i in range(0, len(text), key_dimension):
            text_block = text[i:i + key_dimension]
            if len(text_block) < key_dimension:
                text_block += [0] * (key_dimension - len(text_block))
            ciphertext_block = [0] * key_dimension
            for j in range(key_dimension):
                for k in range(key_dimension):
                    ciphertext_block[j] += (key_inv[j][k] * text_block[k]) % ALPHABET_SIZE
            result += "".join(ALPHABET[char % ALPHABET_SIZE] for char in ciphertext_block)
    return result

cipher = "TFJOXUPOUXYTTRDSXQMONIYPEUFJDQUBGIMOCJQTNBEHCZEKROVBNTWLMVXMOWZLUCHOXYGSKBQGUAOBQZKIXYJIETSWVXHVKCUAOTOFYIZAKJGXKAWGQTRVFDZAJNQDUIWZCMYWNFIUPYMCZXIAKYUCQIAZPIQMGAMGUAKKKHMWKDUXQDUAAKYOWEHLJPWYFKXSARBLLHGAJKTQNTRTPWSCIZASCGSLKVDHTUZSWBNBTJGYYUPQMFSYZAUTOQCDNGQMFSRLRTUWEMKADIVYLTJKFHLKJUWTSSHMHJFGTRIBYIDAHQEPMPIQCROWDYRYZNSPNOJHQVKKTOCBPNFAJNLYJZNVBAYJWRGMCHJPWBDHHTPOXSIJVQWDMSIGMTRVEVXDILKVAYTNUNJXEZLAPGYETRVZNVHSVWLGICDXQFOALDVPASUSYXPFHUWTILUQHTJQVGWFSPAEKBRBNIINYKHNTNUKJVDHVLXQKUZNVQXUOZZOJZYNPIVYSVFVTZMMUUPWTGHRIOWCBKZYAGUMRCKHIQZSIGISPGBXPYXMOAWGAGHQVUWTEIGPBMOMBWIOPQEVKMRQATNBMILHHLVUXGMOUWTZCLBKGWIJHFRNGOSCMUHDWHBB"
key = "6 24 1\n13 16 10\n20 17 15"

## soal nomer 4
# ciphertext = hill_cipher(plaintext, key, "encrypt")
print("Encrypted message:", cipher)
print("\n")
decrypted_message = hill_cipher(cipher, key, "decrypt")
print("Decrypted message:", decrypted_message)