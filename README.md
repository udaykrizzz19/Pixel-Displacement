# Pixel-Displacement


A **Caesar Cipher** is a basic encryption method named after Julius Caesar, who reportedly used it to send secret messages. It involves shifting each letter in a message by a fixed number of positions down or up the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on. This method is easy to implement and understand but offers minimal security because the number of possible shifts (26 for English) is small and easily deciphered.

A **Cipher** is a broader term referring to any algorithm used to encrypt or decrypt information. It transforms readable data, known as plaintext, into an unreadable format, called ciphertext, to protect it from unauthorized access. Ciphers can range from simple substitutions like the Caesar Cipher to complex modern algorithms used in digital encryption to secure data in computing and communication systems.


**Libraries Imported**
cv2: OpenCV library for image processing.
numpy: Library for numerical computations, especially arrays.
matplotlib.pyplot: Library for plotting images.
Functions Defined

**caesar_encrypt(image, key):**
Encrypts the input image using a Caesar cipher.
The encryption is performed by adding a key value to each pixel's intensity and taking the result modulo 256 to ensure the value remains within the valid range of pixel intensities (0-255).

**caesar_decrypt(encrypted_image, key):**
Decrypts the encrypted image using the same key.
The decryption is performed by subtracting the key from each pixel's intensity and taking the result modulo 256 to restore the original pixel values.
Main Program


**Image Loading:**

The script attempts to load a grayscale image (inputImage) from the file path specified by input_filename using OpenCV's imread function with the grayscale flag (0).
If the image fails to load, an error message is printed.


**Image Properties:**

The script calculates the dimensions (height and width) of the image and the total number of pixels, printing these values.


**Key Generation:**

A random key matrix (random_key) with the same dimensions as the image is generated using numpy. Each entry in the matrix is a random integer between 0 and 255.
Image Encryption:

The original image is encrypted using the caesar_encrypt function and the generated random key.


**Image Decryption:**

The encrypted image is decrypted using the caesar_decrypt function and the same random key.
Displaying Images:

The original, encrypted, and decrypted images are displayed side by side using Matplotlib.
The images are saved to the file specified by output_filename.


**Verification:**

The script checks if the decrypted image matches the original image using numpy's array_equal function.
If they match, it prints a success message; otherwise, it prints an error message indicating a discrepancy.
