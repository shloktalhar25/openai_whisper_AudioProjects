# pyrefly: ignore [missing-import]
from transformers import AutoProcessor , AutoModelForSpeechSeq2Seq
# pyrefly: ignore [missing-import]
import librosa
import os






processor = AutoProcessor.from_pretrained("openai/whisper-base")
model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-base")

# load the audio path
audio_path = "noisy_audio.wav"
audio , sr = librosa.load(audio_path , sr =16000)

# convert audio to model input
inputs = processor(audio, sampling_rate=16000, return_tensors="pt",return_attention_mask = True)

# getting the transcription / inferencing
predicted_ids = model.generate(inputs["input_features"],task="transcribe")

# decode the output: convert model output to text.

transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True,clean_up_tokenization_spaces=False)

print("Transcription:", transcription[0])

# Create a folder for generated text if it doesn't exist
output_folder = "generated_texts"
os.makedirs(output_folder, exist_ok=True)

# Save the generated text to a file in the folder
audio_base = os.path.splitext(os.path.basename(audio_path))[0]
output_file = os.path.join(output_folder, f"{audio_base}_transcription.txt")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(transcription[0])

print(f"Saved transcription to: {output_file}")