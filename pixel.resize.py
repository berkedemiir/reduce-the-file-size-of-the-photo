import cv2

# Read the image using imread function
image = cv2.imread('KemalSunal.jpeg')
cv2.imshow('Original Image', image)

# let's downscale the image using new width and height
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)

# Display the resized image
cv2.imshow('Resized Down by defining height and width', resized_down)

# Save the resized image with a specific JPEG compression quality (adjust the value as needed)
cv2.imwrite("ResizedKemalSunal.jpeg", resized_down, [int(cv2.IMWRITE_JPEG_QUALITY), 40])

cv2.waitKey(0)
cv2.destroyAllWindows()








