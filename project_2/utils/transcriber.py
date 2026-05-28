from transformers import pipeline
import torch
from pathlib import Path

# GPU detection
device = 0 if torch.cuda.is_available() else -1

print(f"Using device: {'CUDA' if device == 0 else 'CPU'}")
TRANSCRIPT_DIR = "transcripts"

Path(TRANSCRIPT_DIR).mkdir(exist_ok=True)

# Whisper pipeline
transcriber = pipeline(
    task="automatic-speech-recognition",
    model="openai/whisper-base",
    device=device,

    # Important for long audio
    chunk_length_s=30,
)


def transcribe_audio(audio_path):

    result = transcriber(
        audio_path,

        # Required for long-form audio
        return_timestamps=True
    )

    return result["text"]



def save_transcript(audio_path, transcript_text):

    audio_name = Path(audio_path).stem

    transcript_file = f"{TRANSCRIPT_DIR}/{audio_name}.txt"

    with open(transcript_file, "w", encoding="utf-8") as file:
        file.write(transcript_text)

    return transcript_file