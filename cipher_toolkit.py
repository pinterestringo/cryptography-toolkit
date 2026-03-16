# Caesar + Vigenère Cipher Toolkit

# ============================================================
#   CAESAR CIPHER
# ============================================================

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def caesar_brute_force(text):
    print("\nBrute Force - trying all possible shifts:")
    for shift in range(26):
        print(f"  Shift {shift:2}: {caesar_decrypt(text, shift)}")

# ============================================================
#   VIGENERE CIPHER
# ============================================================

def vigenere_encrypt(text, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# ============================================================
#   MENU
# ============================================================

while True:
    print("\n==========================")
    print("   Cipher Toolkit")
    print("==========================")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Caesar Brute Force")
    print("4. Exit")
    print("==========================")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        text = input("Enter a message: ")
        shift = int(input("Enter shift (1-25): "))
        encrypted = caesar_encrypt(text, shift)
        print(f"  Encrypted: {encrypted}")
        print(f"  Decrypted: {caesar_decrypt(encrypted, shift)}")

    elif choice == "2":
        text = input("Enter a message: ")
        key = input("Enter a keyword (letters only, e.g. KEY): ")
        encrypted = vigenere_encrypt(text, key)
        print(f"  Encrypted: {encrypted}")
        print(f"  Decrypted: {vigenere_decrypt(encrypted, key)}")

    elif choice == "3":
        text = input("Enter encrypted text to brute force: ")
        caesar_brute_force(text)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")
