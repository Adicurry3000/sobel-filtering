import cv2

img = cv2.imread(r"")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

sobel_x = cv2.Sobel(img, -1, 1,0)
sobel_y = cv2.Sobel(img, -1,0,1)

sobel_x_y = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv2.imwrite(r'', sobel_x_y)
cv2.imshow('sobel x and y', sobel_x_y)
cv2.waitKey(0)
