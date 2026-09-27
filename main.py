



import cv2
from ultralytics import YOLO


def openfile(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(e)
    finally:
        print("exiting openfile")
        
openfile("test2.txt")


# Open the default camera
#cap = cv2.VideoCapture("https://wzmedia.dot.ca.gov/D3/20_Dorsey_Dr_NEV20_EB.stream/playlist.m3u8")
cap = cv2.VideoCapture(0)
# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()
# Load a pretrained YOLO model
model = YOLO("yolo11m.pt")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    # Run detection on an image
    results = model(frame, classes = [32], conf = 0.5 )


    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow("Laptop Camera", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()