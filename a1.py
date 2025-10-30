# BEGIN
import cv2
import numpy as np
# IMPORT OpenCV library as cv2
# IMPORT NumPy as np
def apply_color_filter(image, filter_type):
    """
    Apply a specific color filter to the given image and return the result.
    """
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Set green channel to 0
        filtered_image[:, :, 0] = 0  # Set blue channel to 0
        # (Leaves only the red channel visible)
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Set green channel to 0
        filtered_image[:, :, 2] = 0  # Set red channel to 0
        # (Leaves only the blue channel visible)
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Set blue channel to 0
        filtered_image[:, :, 2] = 0  # Set red channel to 0
        # (Leaves only the green channel visible)
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
        # (Ensures pixel values do not overflow beyond 255)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
        # (Ensures pixel values do not go below 0)
    return filtered_image
image_path = "example.jpg"   # File path of input image
image = cv2.imread(image_path)
if image is None:
    print("Error! Image not found!")
else:
    filter_type = "original"  # Default filter
    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("q - Quit")
    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")

cv2.destroyAllWindows()
