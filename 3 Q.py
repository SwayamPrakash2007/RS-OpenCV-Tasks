import cv2

# Read image
img = cv2.imread("c:\\Users\\SWAYAM\\Desktop\\Screenshot 2026-06-12 144515.png")

# Remove noise using Gaussian Blur
denoised = cv2.GaussianBlur(img, (5, 5), 0)

# Save output image
cv2.imwrite("denoised_image.png", denoised)

# Calculate total pixels
height, width, channels = img.shape
total_pixels = height * width

print("Width :", width)
print("Height:", height)
print("Total Pixels:", total_pixels)

cv2.imshow("Original", img)
cv2.imshow("Denoised", denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()