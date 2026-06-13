import cv2
import numpy as np

img = cv2.imread("C:\\Users\\SWAYAM\\Desktop\\Screenshot 2026-06-12 150856.png")

b, g, r = cv2.split(img)

zeros = np.zeros_like(b)

red_img   = cv2.merge([zeros, zeros, r])
green_img = cv2.merge([zeros, g, zeros])
blue_img  = cv2.merge([b, zeros, zeros])

# Remove Green channel
merged = cv2.merge([b, zeros, r])

cv2.imshow("Red Channel", red_img)
cv2.imshow("Green Channel", green_img)
cv2.imshow("Blue Channel", blue_img)
cv2.imshow("Merged Without Green", merged)

cv2.imwrite("red_channel.png", red_img)
cv2.imwrite("green_channel.png", green_img)
cv2.imwrite("blue_channel.png", blue_img)
cv2.imwrite("merged_no_green.png", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()