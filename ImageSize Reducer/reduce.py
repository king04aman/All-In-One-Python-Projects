import cv2

img = cv2.imread('test.jpg')
print(img.shape)

k = 5
width = int((img.shape[1])/k)
height = int((img.shape[0])/k)

scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
print(scaled.shape)

cv2.imshow("Output_Image", scaled)
cv2.waitKey(500)
cv2.destroyAllWindows()

cv2.imwrite('resized_image.jpg', scaled)
