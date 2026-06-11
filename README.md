# youplay

A lightweight CLI utility built in Python to download YouTube playlists and convert them into high-quality 320kbps MP3 files.

## Features
- Full Playlist Extraction
- 320kbps MP3 Audio Transcoding
- Real-time Progress Tracking
- Error Resilience for Private/Deleted Videos

## Prerequisites
- **Arch Linux:** `sudo pacman -S ffmpeg`
- **Ubuntu/Debian:** `sudo apt install ffmpeg`
- **macOS:** `brew install ffmpeg`

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maplelattte/youplay.git
   cd youplay
2. **Configuration**
   ```bash
   python -m venv venv
   source venv/bin/activate.fish  # For Fish shell
   pip install -r requirements.txt #For installing the prerequisites
3. **Finally using it**
   ```bash
   cd src
   python downloader.py --url "YOUR_PLAYLIST_URL"
