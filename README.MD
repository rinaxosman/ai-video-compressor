
# 🧠 AI Video Compressor

A simple web app that compresses `.mp4` videos to under **10MB** so they can be shared on platforms like **Discord**. Great for users who want quick compression without installing software.

> ✅ MVP Version – Free, lightweight, and easy to use!

---

## ✨ Features
- 📤 Upload your `.mp4` file (up to 100MB)
- 📉 Compresses videos to ≤10MB using FFmpeg
- 💧 Adds watermark for free-tier users
- 🔁 2 free compressions/month (tracked via browser)
- ⚡ No login required

---

## 🚀 Getting Started

### 🔧 Backend (Python + Flask)
Make sure you have Python 3.9+ and [FFmpeg](https://ffmpeg.org/download.html) installed.

```bash
# Clone the repo
git clone https://github.com/rinaxosman/ai-video-compressor.git
cd ai-video-compressor/backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

By default, the backend runs at `http://localhost:5000`.

---

### 🌐 Frontend
```bash
# Navigate to the frontend directory
cd ../frontend

# Open the index.html file in your browser
open index.html  # Or just double-click it
```

Or connect it to Flask with a static route for production.

---

## 🛠 Tech Stack
- **Frontend**: HTML, JavaScript
- **Backend**: Python (Flask)
- **Video Processing**: FFmpeg
- **Storage**: Local (temp folder)
- **Deployment**: Optional – Render, Replit, or Railway

---

## 📦 Roadmap
- [x] MVP: Upload + Compress + Watermark
- [ ] Stripe integration
- [ ] User accounts + compression history
- [ ] Cloud-based file storage (e.g. S3)
- [ ] AI-based intelligent compression

---

## 💡 Example Use Cases
- Send gameplay clips on Discord
- Share lecture/tutorial videos easily
- Reduce file size for email attachments

---

## 🧠 Credits
Built by [@rinaxosman](https://github.com/rinaxosman)  
