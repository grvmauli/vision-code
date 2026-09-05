import cv2
from pathlib import Path
import numpy as np

import matplotlib.pyplot as plt





INPUT = Path("images/input.jpg")

OUTPUT = Path("output")



OUTPUT.mkdir(exist_ok=True)





# 1. Load image

image = cv2.imread(str(INPUT))



if image is None:
    raise FileNotFoundError(f"Could not read image: {INPUT}")



# 2. Convert to grayscale

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# 3. Reduce high-frequency noise

blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)



# 4. Sobel gradients

sobel_x = cv2.Sobel(

blurred,

cv2.CV_64F,

1,

0,

ksize=3

)



sobel_y = cv2.Sobel(

blurred,

cv2.CV_64F,

0,

1,

ksize=3

)



# 5. Calculate gradient magnitude

magnitude = cv2.magnitude(

sobel_x.astype(np.float32),

sobel_y.astype(np.float32)

)



magnitude = cv2.normalize(

magnitude,

None,

0,

255,

cv2.NORM_MINMAX

).astype(np.uint8)



# 6. Canny edge detection

canny = cv2.Canny(

blurred,

threshold1=50,

threshold2=150,

apertureSize=3,

L2gradient=True

)



# 7. Save results

cv2.imwrite(str(OUTPUT / "grayscale.png"), gray)

cv2.imwrite(str(OUTPUT / "sobel_magnitude.png"), magnitude)

cv2.imwrite(str(OUTPUT / "canny.png"), canny)



# 8. Display comparison

fig, axes = plt.subplots(1, 3, figsize=(15, 5))



axes[0].imshow(gray, cmap="gray")

axes[0].set_title("Grayscale")

axes[0].axis("off")



axes[1].imshow(magnitude, cmap="gray")

axes[1].set_title("Sobel Gradient Magnitude")

axes[1].axis("off")



axes[2].imshow(canny, cmap="gray")

axes[2].set_title("Canny")

axes[2].axis("off")



plt.tight_layout()

plt.savefig(OUTPUT / "edge_comparison.png", dpi=150)

plt.show()

sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
magnitude = cv2.magnitude(

sobel_x.astype(np.float32),

sobel_y.astype(np.float32)

)

canny = cv2.Canny(

blurred,

threshold1=50,

threshold2=150,

apertureSize=3,

L2gradient=True

)