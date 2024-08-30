def caesar_cipher(text, shift, encrypt=True):
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift if encrypt else -shift
            ascii_offset = 65 if char.isupper() else 97
            
            # Shift character and wrap around if necessary
            shifted_char = chr(((ord(char) - ascii_offset + shift_amount) % 26) + ascii_offset)
            result += shifted_char
        else:
            result += char  # Non-alphabetical characters remain unchanged
    
    return result

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (0-25): "))
    
    if choice == 'e':
        encrypted_message = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted Message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()

