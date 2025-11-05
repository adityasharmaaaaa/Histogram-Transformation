import cv2                      # OpenCV library for image processing
import numpy as np              # NumPy for numerical operations
import matplotlib.pyplot as plt # Matplotlib for plotting histograms and images

# Step 1: Read the image
# Replace 'input.jpg' with the path to your image file
image = cv2.imread('Project 1/125686-2560x1440-desktop-hd-game-of-thrones-background.jpg', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded properly
if image is None:
    print("Error: Image not found or path is incorrect.")
    exit()

# Step 2: Calculate the original histogram
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])

# Step 3: Apply Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Step 4: Calculate histogram after transformation
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# Step 5: Display images and their histograms
plt.figure(figsize=(12, 6))

# Original image and histogram
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.plot(hist_original, color='black')
plt.title('Original Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Equalized image and histogram
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Histogram Equalized Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.plot(hist_equalized, color='black')
plt.title('Equalized Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Step 6: Optionally, save the result
cv2.imwrite('equalized_output.jpg', equalized_image)

print("Histogram equalization completed and saved as 'equalized_output.jpg'.")
