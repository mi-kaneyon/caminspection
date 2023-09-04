import cv2
import numpy as np

# Initialize the video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1920)  # Set the width
cap.set(4, 1080)  # Set the height

# Initialize the line positions
horizontal_line_pos = int(1080 / 2)
vertical_line_pos = int(1920 / 2)

while True:
    ret, frame = cap.read()
    
    # Display instructions
    cv2.putText(frame, "WX(Horizon) AD(Vertical)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Draw horizontal and vertical line
    cv2.line(frame, (0, horizontal_line_pos), (1920, horizontal_line_pos), (255, 0, 0), 2)
    cv2.line(frame, (vertical_line_pos, 0), (vertical_line_pos, 1080), (0, 0, 255), 2)
    
    # Show the frame with lines
    cv2.imshow('Camera with Lines', frame)
    
    # Display instructions
    cv2.displayOverlay('Camera with Lines', 'Press W, X, A, D to move lines, Q to quit', 5000)
    
    # Key events for line movement and exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('w'):
        horizontal_line_pos -= 5
    if key == ord('x'):
        horizontal_line_pos += 5
    if key == ord('a'):
        vertical_line_pos -= 5
    if key == ord('d'):
        vertical_line_pos += 5
    if key == ord('q'):
        break

# Release the capture and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
