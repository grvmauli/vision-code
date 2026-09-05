import cv2

import numpy as np

import matplotlib.pyplot as plt



image = cv2.imread("sample.jpg")



if image is None:
    raise FileNotFoundError("Could not find input.jpg")



image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



print("Image shape:", image.shape)

print("RGB channels:", image_rgb.shape)

print("HSV channels:", hsv.shape)

print("Grayscale range:", gray.min(), "to", gray.max())

histogram = cv2.calcHist(

[gray],

[0],

None,

[256],

[0, 256]

)



print("Histogram bins:", len(histogram))

print("Total pixels:", int(histogram.sum()))

cdf = histogram.cumsum()



print("First CDF value:", cdf[0])

print("Final CDF value:", cdf[-1])

cdf_min = cdf[cdf > 0].min()

total_pixels = gray.size



lookup_table = np.round(

(cdf - cdf_min) /

(total_pixels - cdf_min) *

255

).clip(0, 255).astype(np.uint8)



equalized_manual = lookup_table[gray]

equalized_opencv = cv2.equalizeHist(gray)



difference = cv2.absdiff(

equalized_manual,

equalized_opencv

)



print("Maximum pixel difference:",

int(difference.max()))



print("Mean pixel difference:",

float(difference.mean()))

hsv_equalized = hsv.copy()



hsv_equalized[:, :, 2] = cv2.equalizeHist(

hsv_equalized[:, :, 2]

)



enhanced_bgr = cv2.cvtColor(

hsv_equalized,

cv2.COLOR_HSV2BGR

)



enhanced_rgb = cv2.cvtColor(

enhanced_bgr,

cv2.COLOR_BGR2RGB

)

cv2.imwrite("equalized_gray.png", equalized_manual)

cv2.imwrite("enhanced_color.png", enhanced_bgr)

plt.figure(figsize=(12, 8))



plt.subplot(2, 2, 1)

plt.imshow(image_rgb)

plt.title("Original")

plt.axis("off")



plt.subplot(2, 2, 2)

plt.imshow(equalized_manual, cmap="gray")

plt.title("Equalized Grayscale")

plt.axis("off")



plt.subplot(2, 2, 3)

plt.hist(gray.ravel(), 256, [0, 256])

plt.title("Original Histogram")



plt.subplot(2, 2, 4)

plt.hist(equalized_manual.ravel(), 256, [0, 256])

plt.title("Equalized Histogram")



plt.tight_layout()

plt.savefig("histogram_comparison.png", dpi=150)

plt.show()