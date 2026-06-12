'''

B) Correct
gray_frame is a single-channel grayscale image. When you draw:

cv2.rectangle(gray_frame, (10, 10), (100, 100), (0, 255, 0), 3)

OpenCV cannot display a green rectangle on a grayscale image. The color tuple (0,255,0) will effectively be interpreted as a grayscale intensity, so the rectangle will appear in a shade of gray, not green.


A) Incorrect
cv2.imread() loads images in BGR (Blue, Green, Red) format by default, not RGB.

C) Correct
For a static image:

cv2.waitKey(1)

waits only 1 millisecond. After that, the script ends and the window usually closes immediately.

For viewing a static image, it should be:

cv2.waitKey(0)

which waits until a key is pressed.


D) Incorrect
In:

cv2.rectangle(gray_frame, (10, 10), (100, 100), ...)

(10,10) and (100,100) are the top-left and bottom-right corners of the rectangle, respectively. They are not the center point and width/height.


'''
