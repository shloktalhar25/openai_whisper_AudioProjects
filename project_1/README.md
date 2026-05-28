## model : openai/whisper-base
## platform : huggingface


## model use:
Whisper is an open-source pretrained model from open-ai use for Automatic speach recognition [ASR] and speech translation.

# trained on massive hrs or data(680k), no need to finetune.



### Regarding the training:
1.The English-only models were trained on the task of speech recognition. The multilingual models were trained on both speech recognition and speech translation

2.For speech recognition, the model predicts transcriptions in the same language as the audio. For speech translation, the model predicts transcriptions to a different language to the audio.



### details on output geneerated:
<|startoftranscript|> <|en|> <|transcribe|> <|notimestamps|>



### import Libraries:

AutoProcessor , 
AutoModelForSpeechSeq2Seq
