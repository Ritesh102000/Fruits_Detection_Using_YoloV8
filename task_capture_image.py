import cv2
import os

# Set the folder to save images
save_folder = "captured_images"
os.makedirs(save_folder, exist_ok=True)

# Find the next available file number
existing_files = [int(f.split(".")[0]) for f in os.listdir(save_folder) if f.endswith(".jpg")]
next_index = max(existing_files) + 1 if existing_files else 1

# Open the webcam
cap = cv2.VideoCapture(0)

print("Press 'SPACE' to capture an image, 'Q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam - Press 'SPACE' to Capture", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord(" "):  # Press SPACE to capture
        filename = os.path.join(save_folder, f"{next_index}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        next_index += 1

    elif key == ord("q"):  # Press 'Q' to exit
        break

cap.release()
cv2.destroyAllWindows()
 

