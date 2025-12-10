from detection import zero_shot_detect
from tracking import track_objects
import cv2

def main():
    print("Starting Zero-Shot Object Detection & Tracking System...")

    video_path = "sample_input.mp4"  # replace with your video
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Zero-shot detection
        detections = zero_shot_detect(frame)

        # Object tracking
        tracked_objects = track_objects(detections)

        # Display results
        for obj in tracked_objects:
            x, y, w, h = obj["bbox"]
            label = obj["label"]

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        cv2.imshow("ZSOD Tracking", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
