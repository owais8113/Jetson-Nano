import cv2
import easyocr
import numpy as np

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Initialize the video capture (0 for the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame")
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Use EasyOCR to detect text
    result = reader.readtext(rgb_frame)

    # Draw bounding boxes and text on the frame
    for (bbox, text, prob) in result:
        # Get the coordinates of the bounding box
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        # Draw the bounding box
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

        # Display the text
        cv2.putText(frame, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with bounding boxes and text
    cv2.imshow('Real-Time Text Detection', frame)

    # Press 'q' to quit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
