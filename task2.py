from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image and convert it to RGB format
    image = Image.open(input_path).convert('RGB')
    data = np.array(image, dtype=np.uint8)
    
    # Encrypt the pixels using the key (simple arithmetic operation)
    encrypted_data = (data.astype(np.int32) + key) % 256
    encrypted_data = encrypted_data.astype(np.uint8)
    
    # Create an encrypted image from the modified pixel data
    encrypted_image = Image.fromarray(encrypted_data)
    encrypted_image.save(output_path)
    print("Image encrypted and saved as:", output_path)

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image and convert it to RGB format
    encrypted_image = Image.open(input_path).convert('RGB')
    encrypted_data = np.array(encrypted_image, dtype=np.uint8)
    
    # Decrypt the pixels using the key (reverse the arithmetic operation)
    decrypted_data = (encrypted_data.astype(np.int32) - key) % 256
    decrypted_data = decrypted_data.astype(np.uint8)
    
    # Create a decrypted image from the modified pixel data
    decrypted_image = Image.fromarray(decrypted_data)
    decrypted_image.save(output_path)
    print("Image decrypted and saved as:", output_path)

# Example usage
key = 50  # Choose an encryption key (any integer value)
encrypt_image('input_image.png', 'encrypted_image.png', key)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key)
