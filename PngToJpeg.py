import cv2



image = cv2.imread("KemalSunal.png")
#imread is use to read an image from a location

cv2.imwrite("KemalSunal.jpeg", image)

cv2.waitKey()
cv2.destroyAllWindows()