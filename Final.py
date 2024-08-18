import cv2
import numpy as np
import matplotlib.pyplot as plt

def caesar_encrypt(image, key):
    key = key % 256
    encrypted_image = (image + key) % 256
    return encrypted_image

def caesar_decrypt(encrypted_image, key):
    key = key % 256
    decrypted_image = (encrypted_image - key) % 256
    return decrypted_image

input_filename = '/content/Test Image 4.jpg'
output_filename = 'output_images.png'

# Load the input image
inputImage = cv2.imread(input_filename, 0)

# Check if the image was loaded successfully
if inputImage is None:
    print(f"Error: Unable to load image {input_filename}")
else:
    # Get image dimensions, no of pixels
    height, width = inputImage.shape[:2]
    pixels = height * width

    # Print the computed values
    print(f"Image Dimensions - Height: {height}, Width: {width}")
    print(f"Number of Pixels: {pixels} \n\n")

    # Generate a random key with the same dimensions as the image
    random_key = np.random.randint(0, 256, (height, width), dtype=np.uint8)

    # Print the random key
    print("Random Key:")
    print(random_key)
    print("\n")

    # Encrypt the image using Caesar cipher encryption
    encrypted_image = caesar_encrypt(inputImage, random_key)

    # Decrypt the image using Caesar cipher decryption
    decrypted_image = caesar_decrypt(encrypted_image, random_key)

    # Display the images
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    axs[0].imshow(inputImage, cmap='gray')
    axs[0].set_title('Original Image')
    axs[1].imshow(encrypted_image, cmap='gray')
    axs[1].set_title('Encrypted Image')
    axs[2].imshow(decrypted_image, cmap='gray')
    axs[2].set_title('Decrypted Image')

    for ax in axs:
        ax.axis('off')

    plt.savefig(output_filename)
    plt.show()

    # Check if the decrypted image is the same as the original image
    if np.array_equal(inputImage, decrypted_image):
        print("\nSuccess: The decrypted image matches the original image.")
    else:
        print("\nError: The decrypted image does not match the original image.")
