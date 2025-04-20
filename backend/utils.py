import subprocess
import os
import time

import subprocess

def compress_video(input_path, output_path):
    ffmpeg_path = r"C:\Users\rinax\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"

    command = [
    ffmpeg_path, "-i", input_path,
    "-vcodec", "libx264",
    "-crf", "35",
    "-preset", "ultrafast",
    "-acodec", "aac",
    "-b:a", "64k", 
    "-movflags", "+faststart",
    "-fs", "10M", 
    "-y", output_path
    ]

    print("⚙️ Running FFmpeg command:")
    print(" ".join(command))

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ FFmpeg failed with error:")
        print(result.stderr)
        raise Exception("FFmpeg compression failed")
    else:
        print("✅ FFmpeg succeeded")
        print(result.stdout)


def clean_old_files(directory, age_seconds=3600):
    now = time.time()
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and now - os.path.getmtime(path) > age_seconds:
            os.remove(path)
            print(f"Removed old file: {path}")