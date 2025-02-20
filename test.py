import os
import random
import cv2
import tkinter as tk
from tkinter import filedialog

class RandomVideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy Kiểm Tra Độ Đẹp Gái")
        
        self.label = tk.Label(root, text="Máy Kiểm Tra Độ Đẹp Gái", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.test_button = tk.Button(root, text="Test", command=self.play_random_video)
        self.test_button.pack(pady=20)
        
        self.video_folder = filedialog.askdirectory(title="Select Folder with Videos")
        
    def play_random_video(self):
        if not self.video_folder:
            return
        
        videos = [f for f in os.listdir(self.video_folder) if f.endswith(('.mp4', '.mkv', '.avi'))]
        if not videos:
            print("No videos found in the selected folder.")
            return
        
        random_video = random.choice(videos)
        video_path = os.path.join(self.video_folder, random_video)
        
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"Error opening video file: {video_path}")
            return
        
        cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    player = RandomVideoPlayer(root)
    root.mainloop()