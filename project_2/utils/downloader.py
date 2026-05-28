# we shall write the code to downlaod the youtube video here
import yt_dlp
from pathlib import Path


DOWNLOAD_DIR = "downloads"


def download_audio(youtube_url):
    Path(DOWNLOAD_DIR).mkdir(exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",

        # Output filename
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",

        # Convert audio to mp3
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],

        "quiet": False,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)

        # Final mp3 filename
        safe_title = Path(ydl.prepare_filename(info)).stem

        final_file = f"{DOWNLOAD_DIR}/{safe_title}.mp3"

    return final_file