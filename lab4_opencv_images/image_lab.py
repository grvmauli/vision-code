import cv2





INPUT_FILE = "sample.jpg"

OUTPUT_FILE = "processed_image.jpg"

CROP_FILE = "crop.jpg"

RESIZED_FILE = "resized.jpg"





# 1. Load

image = cv2.imread(INPUT_FILE)



if image is None:
    raise FileNotFoundError(f"Could not load image: {INPUT_FILE}")





# 2. Inspect

height, width, channels = image.shape



print("=== IMAGE INFORMATION ===")

print(f"Width: {width}")

print(f"Height: {height}")

print(f"Channels: {channels}")

print(f"Data type: {image.dtype}")





# 3. Inspect one pixel

print("\n=== PIXEL INFORMATION ===")

print("Pixel [100, 100]:", image[100, 100])





# 4. Modify a small region

image[100:200, 100:200] = [0, 255, 0]





# 5. Crop

crop = image[100:500, 100:600]



if not cv2.imwrite(CROP_FILE, crop):
    raise RuntimeError("Failed to save crop")





# 6. Resize

resized = cv2.resize(

image,

(800, 600),

interpolation=cv2.INTER_AREA

)



if not cv2.imwrite(RESIZED_FILE, resized):
    raise RuntimeError("Failed to save resized image")





# 7. Save final result

if not cv2.imwrite(OUTPUT_FILE, image):
    raise RuntimeError("Failed to save processed image")





print("\n=== SUCCESS ===")

print(f"Created: {OUTPUT_FILE}")

print(f"Created: {CROP_FILE}")

print(f"Created: {RESIZED_FILE}")