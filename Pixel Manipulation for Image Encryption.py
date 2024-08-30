from PIL import Image
import numpy as np

def encrypt_image(image_path, key=50):
    # Load image
    image = Image.open("C:\Users\HP PAVILION LAP\OneDrive\Desktop\vineet kadam\python  vs code\projects\berserker.jpg")
    image_array = np.array(berserker.jpg)

    # Apply a simple encryption algorithm: Add a key value to each pixel
    encrypted_array = ("C:\Users\HP PAVILION LAP\OneDrive\Desktop\vineet kadam\python  vs code\projects\berserker.jpg" + key) % 256  # Keeping pixel values in the 0-255 range

    # Convert back to image and save
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    encrypted_image.save("encrypted_image.png")
    print("Encryption complete. Image saved as 'encrypted_image.png'")

def decrypt_image(image_path, key=50):
    # Load the encrypted image
    encrypted_image = Image.open("C:\Users\HP PAVILION LAP\OneDrive\Desktop\vineet kadam\python  vs code\projects\berserker.jpg")
    encrypted_array = np.array(encrypted_image)

    # Apply decryption: Subtract the key value to each pixel
    decrypted_array = (encrypted_array - key) % 256  # Keeping pixel values in the 0-255 range

    # Convert back to image and save
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    decrypted_image.save("decrypted_image.png")
    print("Decryption complete. Image saved as 'decrypted_image.png'")

# Example usage:
# Encrypt an image
encrypt_image("your_image.png", key=50)

# Decrypt the image
decrypt_image("encrypted_image.png", key=50)
