import cv2
import numpy as np

# Define color ranges and their corresponding color names
color_ranges = {
    'red': ([0, 100, 100], [10, 255, 255]),  # Red
    'green': ([36, 100, 100], [86, 255, 255]),  # Green
    'blue': ([100, 100, 100], [140, 255, 255]),  # Blue
    'yellow': ([20, 100, 100], [40, 255, 255]),  # Yellow
    'orange': ([5, 100, 100], [15, 255, 255])  # Orange
}

# Function to find the most dominant color and its name
def get_dominant_color(image):
    # Convert image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    max_percentage = 0
    dominant_color_name = None

    # Iterate through the color ranges and find the dominant color
    for color_name, (lower_bound, upper_bound) in color_ranges.items():
        # Create a mask to extract the specific color range
        mask = cv2.inRange(hsv_image, np.array(lower_bound), np.array(upper_bound))

        # Calculate the percentage of pixels that belong to the color range
        percentage = np.sum(mask == 255) / (mask.shape[0] * mask.shape[1]) * 100

        # Update dominant color if percentage is higher
        if percentage > max_percentage:
            max_percentage = percentage
            dominant_color_name = color_name

    return dominant_color_name, max_percentage

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Apply color detection
    dominant_color_name, dominant_color_percentage = get_dominant_color(frame)

    # Display the frame
    cv2.putText(frame, f'Dominant Color: {dominant_color_name} ({dominant_color_percentage:.2f}%)', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('Color Detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
