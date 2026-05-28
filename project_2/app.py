import sys
from utils.downloader import download_audio
from utils.transcriber import (
    transcribe_audio,
    save_transcript
)



# Default test URL if none is provided
DEFAULT_TEST_URL = "https://www.youtube.com/watch?v=aqz-KE-bpKQ"

if len(sys.argv) > 1:
    youtube_url = sys.argv[1]
else:
    user_input = input(f"Enter YouTube URL [default: {DEFAULT_TEST_URL}]: ").strip()
    youtube_url = user_input if user_input else DEFAULT_TEST_URL

print(f"\nProcessing URL: {youtube_url}")

print("\nDownloading audio...")
audio_file = download_audio(youtube_url)

print(f"\nDownloaded File: {audio_file}")

print("\nStarting transcription (this might take a few moments)...")
transcript = transcribe_audio(audio_file)

print("\nTranscript:")
print("=" * 40)
print(transcript)
print("=" * 40)

saved_file = save_transcript(audio_file, transcript)

print(f"\nTranscript saved to:\n{saved_file}")