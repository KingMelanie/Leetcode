def rc4(key, plaintext):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    ciphertext = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        ciphertext.append(chr(ord(char) ^ k))

    return "".join(ciphertext)

def encrypt(key, plaintext):
    return rc4(key, plaintext)

def decrypt(key, ciphertext):
    return rc4(key, ciphertext)

def main():
    key = "brucelee"
    plaintext = "attackatdawn"
    ciphertext = encrypt(key, plaintext)
    print("\nCiphertext:", ciphertext)

    decrypted_plaintext = decrypt(key, ciphertext)
    print("\nDecrypted plaintext:", decrypted_plaintext)

if __name__ == "__main__":
    main()