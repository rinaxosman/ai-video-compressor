import subprocess
import os
import time

def compress_video(input_path, output_path):
    cmd = [
        "ffmpeg", "-i", input_path,
        "-vcodec", "libx264", "-crf", "30",
        "-preset", "veryfast",
        "-y", output_path
    ]
    subprocess.run(cmd, check=True)

def clean_old_files(directory, age_seconds=3600):
    now = time.time()
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and now - os.path.getmtime(path) > age_seconds:
            os.remove(path)
            print(f"Removed old file: {path}")