import cv2

import torch

# Vision Lab - Basic image testing scriptgit

print("=== Vision Workstation Test ===")

print("OpenCV version:", cv2.__version__)

print("PyTorch version:", torch.__version__)

print("CUDA available:", torch.cuda.is_available())



image = cv2.imread("test.jpg")



if image is None:

	print("Image test: waiting for test.jpg")

else:

	print("Image test: SUCCESS")

print("Image dimensions:", image.shape)
