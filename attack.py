def brute_force(cipher_text):
    print("\nBrute Force Results:\n")

    for shift in range(1, 26):
        decrypted = ""

        for char in cipher_text:
            if char.isalpha():
                base = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted += char

        print(f"Shift {shift}: {decrypted}")