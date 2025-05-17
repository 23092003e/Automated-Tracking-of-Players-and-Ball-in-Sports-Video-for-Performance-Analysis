import os
import cv2

def extract_frames(video_path: str, output_folder: str, skip: int = 1) -> int:
    """
    Extract frames from video and save to output_folder. Returns number of frames extracted.
    """
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0
    saved = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % skip == 0:
            cv2.imwrite(os.path.join(output_folder, f"frame_{saved:06d}.jpg"), frame)
            saved += 1
        count += 1
    cap.release()
    return saved
video_path = r"C:\Users\ADMIN\Desktop\Deep Learning\Automated-Tracking-of-Players-and-Ball-in-Sports-Video-for-Performance-Analysis\data\video.mp4"
extract_frames(video_path, "output_frames", skip=5)