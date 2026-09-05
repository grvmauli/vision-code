import cv2

import numpy as np



image = cv2.imread("sample.jpg")



if image is None:
    raise FileNotFoundError("Could not load input.jpg")



height, width = image.shape[:2]



# Translation: move the image 100 pixels right

# and 50 pixels downward.

translation = np.float32([

[1, 0, 100],

[0, 1, 50]

])



translated = cv2.warpAffine(

image,

translation,

(width, height)

)



# Rotation around the image center.

center = (width / 2, height / 2)



rotation = cv2.getRotationMatrix2D(

center,

20,

1.0

)



rotated = cv2.warpAffine(

image,

rotation,

(width, height)

)



# Affine transformation using three corresponding points.

source_points = np.float32([

[0, 0],

[width - 1, 0],

[0, height - 1]

])



destination_points = np.float32([

[50, 30],

[width - 80, 60],

[80, height - 40]

])



affine_matrix = cv2.getAffineTransform(

source_points,

destination_points

)



warped = cv2.warpAffine(

image,

affine_matrix,

(width, height)

)



cv2.imwrite("translated.jpg", translated)

cv2.imwrite("rotated.jpg", rotated)

cv2.imwrite("affine_warped.jpg", warped)



print("Transformation pipeline completed.")

print("Affine matrix:")

print(affine_matrix)

shear_matrix = np.float32([

[1, 0.25, 0],

[0, 1, 0]

])



sheared = cv2.warpAffine(

image,

shear_matrix,

(width, height)

)



cv2.imwrite("sheared.jpg", sheared)