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