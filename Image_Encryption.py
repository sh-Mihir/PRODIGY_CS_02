# Task 2

from PIL import Image
import numpy as np

print()
print(
    "-------------------- Welcome to Image encryption and Decryption Program --------------------"
)
print()


# Load an image specified by image path
def load_image(img_path):
    try:
        image = Image.open(img_path)
        return image
    except FileNotFoundError:
        print(f"The file {img_path} was not found.")
        return None


# Save the image to the specified file path
def save_image(image, path):
    try:
        image.save(path)
    except Exception as e:
        print(f"Error: Could not save the image to {path}. {e}")


# Generate key image for encryption
def generate_key_image(image):
    try:
        np_image = np.array(image)
        key_image = np.random.randint(0, 256, np_image.shape, dtype=np.uint8)
        return Image.fromarray(key_image)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Encrypt specified image using key image
def encrypt_image(image, key_image):
    try:
        np_image = np.array(image)
        np_key_image = np.array(key_image)
        encrypted_image = np.bitwise_xor(np_image, np_key_image)
        return Image.fromarray(encrypted_image)
    except Exception as e:
        print(f"Error: {e}")
        return None


# Decrypt an encrypted image using the same key image used at the time of an encryption
def decrypt_image(encrypted_image, key_image):
    try:
        np_encrypted_image = np.array(encrypted_image)
        np_key_image = np.array(key_image)
        decrypted_image = np.bitwise_xor(np_encrypted_image, np_key_image)
        return Image.fromarray(decrypted_image)
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    user_input = (
        input("Do you want to encrypt or decrypt an image (e/d): ").strip().lower()
    )

    if user_input == "e":
        img_path = input("Enter the path of an image to encrypt: ")
        key_path = input("Enter the path to save the key image: ")
        encrypted_path = input("Enter the path to save an encrypted image: ")

        # Load the image
        image = load_image(img_path)

        # Generate a key image
        key_image = generate_key_image(image)
        save_image(key_image, key_path)
        print(f"Key image saved to {key_path}.")

        # Encrypt the image
        encrypted_image = encrypt_image(image, key_image)
        save_image(encrypted_image, encrypted_path)
        print(f"Encrypted image saved to {encrypted_path}.")

    elif user_input == "d":
        key_path = input("Enter the path of the key image: ")
        encrypted_path = input("Enter the path of an encrypted image to decrypt: ")
        decrypted_path = input("Enter the path to save the decrypted image: ")

        encrypted_image = Image.open(encrypted_path)
        key_image = Image.open(key_path)

        # Decrypt the image
        decrypted_image = decrypt_image(encrypted_image, key_image)
        save_image(decrypted_image, decrypted_path)
        print(f"Decrypted image saved to {decrypted_path}.")

    else:
        print("Invalid input! Enter e for encryption or d for decryption.")


if __name__ == "__main__":
    main()
