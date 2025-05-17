import os
from yt_dlp import YoutubeDL

def download_video(url: str, output_path: str) -> None:
    """
    Download video from URL using yt-dlp.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': output_path
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f"Video downloaded to {output_path}")
        
