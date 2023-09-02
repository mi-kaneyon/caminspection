
import cv2
import numpy as np

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    # Set resolution (change these values according to your camera's capability)
    width = 640
    height = 480
    cap.set(3, width)
    cap.set(4, height)
    
    # Initialize position of lines
    horizon_line_pos = height // 2
    vertical_line_pos = width // 2
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Draw lines
        cv2.line(frame, (0, horizon_line_pos), (width, horizon_line_pos), (0, 0, 255), 2)
        cv2.line(frame, (vertical_line_pos, 0), (vertical_line_pos, height), (0, 0, 255), 2)
        
        # Display instructions
        cv2.putText(frame, "WX(Horizon) AD(Vertical)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Camera Control', frame)
        
        # Keyboard controls
        key = cv2.waitKey(1)
        if key == ord('w'):
            horizon_line_pos = max(horizon_line_pos - 5, 0)
        elif key == ord('x'):
            horizon_line_pos = min(horizon_line_pos + 5, height)
        elif key == ord('a'):
            vertical_line_pos = max(vertical_line_pos - 5, 0)
        elif key == ord('d'):
            vertical_line_pos = min(vertical_line_pos + 5, width)
        elif key == ord('q'):
            break
    
    # Release the capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
