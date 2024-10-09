def caesar_cipher(text, shift, mode):
    # This will store the result of encryption or decryption
    result = ""

    # Adjust the shift for decryption if needed
    if mode == "decrypt":
        shift = -shift

    # Traverse through each character in the text
    for char in text:
        # Encrypt/decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not an alphabetic character, keep it as it is
        else:
            result += char

    return result

# Main program
def main():
    print("Caesar Cipher Program")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("\nEnter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift, "encrypt")
            print("Encrypted message:", encrypted_message)

        elif choice == '2':
            message = input("\nEnter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift, "decrypt")
            print("Decrypted message:", decrypted_message)

        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
