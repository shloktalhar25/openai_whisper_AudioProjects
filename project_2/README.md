## 1. we can downlaod the youtube video using yt-dlp ,dlp works by downlaoding the yt video in audio stream format (best suited) and then ffmpeg converts that to .mp3 format for better and general usecase.
# The audio stream format (.webm) gets automatically deleted and the mp3 remains unchanged.

# here is the flow:
```
YouTube Audio Stream
        ↓
Temporary webm/m4a
        ↓
FFmpeg Conversion
        ↓
Final MP3
```
## Its good for samll time audios , but if we want to transcribe long audio then we might have to chunk.

