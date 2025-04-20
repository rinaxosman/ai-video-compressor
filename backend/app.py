from flask import Flask, request, send_from_directory, jsonify
import os
import uuid
from utils import compress_video, clean_old_files

app = Flask(__name__)
UPLOAD_FOLDER = "static/output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "AI Video Compressor API is running. Use the frontend to upload a video."

@app.route("/compress", methods=["POST"])
def compress():
    clean_old_files(UPLOAD_FOLDER)

    file = request.files.get("video")
    if not file or not file.filename.endswith(".mp4"):
        return jsonify({"error": "Invalid file"}), 400

    input_path = os.path.join(UPLOAD_FOLDER, f"input_{uuid.uuid4().hex}.mp4")
    output_path = os.path.join(UPLOAD_FOLDER, f"compressed_{uuid.uuid4().hex}.mp4")

    file.save(input_path)

    try:
        compress_video(input_path, output_path)
        filename = os.path.basename(output_path)
        return jsonify({"url": f"/download/{filename}"})
    except Exception as e:
        print("Compression error:", e)
        return jsonify({"error": str(e)}), 500

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
