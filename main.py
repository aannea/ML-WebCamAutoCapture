import cv2
import mediapipe as mp
import os
import time
mp_hands = mp.solutions.hands
def detect_pose(landmarks):
    if landmarks:
        # Pose "OK"
        if (
            landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y >
            landmarks[mp.solutions.hands.HandLandmark.WRIST].y and
            landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y >
            landmarks[mp.solutions.hands.HandLandmark.WRIST].y and
            landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP].x <
            landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].x and
            landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP].y <
            landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y
        ):
            return "OK"

        # Pose "Thumbs Up"
        if (
            landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP].y <
            landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y and
            landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP].x >
            landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].x
        ):
            return "Thumbs Up"

        # Pose "Peace"
        if (
            landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y <
            landmarks[mp.solutions.hands.HandLandmark.WRIST].y and
            landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y <
            landmarks[mp.solutions.hands.HandLandmark.WRIST].y
        ):
            return "Peace"

        # Pose "Rock"
        if (
            landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP].y >
            landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y and
            landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y >
            landmarks[mp.solutions.hands.HandLandmark.WRIST].y
        ):
            return "Rock"
    return None

def capture_images(output_folder, num_images=1):
    # Membuat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    last_capture_time = 0

    while True:
        ret, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        text_color = (255, 255, 255)
        text_position = (50, 50)
        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0].landmark
            pose = detect_pose(landmarks)
            if pose:
                current_time = time.time()
                if current_time - last_capture_time > 3:
                    image_path = os.path.join(output_folder, f"captured_image_{time.time()}.jpg")
                    cv2.imwrite(image_path, frame)
                    print("Diambil!")
                    cv2.putText(frame, "Diambil!", text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
                    last_capture_time = current_time
        cv2.imshow("Webcam", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_folder = "captured_images"
    capture_images(output_folder)