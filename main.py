# dependencies.
from libretranslatepy import LibreTranslateAPI
from gtts import gTTS
import speech_recognition
from pydub import AudioSegment

r = speech_recognition.Recognizer()
lt = LibreTranslateAPI("https://translate.argosopentech.com/")

# audio extractioin from mp4.
sound = AudioSegment.from_mp3(input("Enter path to mp4/mp3 file: "))
sound.export("source_audio.wav", format="wav")

# speech to text.
with speech_recognition.AudioFile("source_audio.wav") as source:
    audio = r.record(source)
source_text = r.recognize_google(audio)

# text translation.
target_text = lt.translate(source_text, "en", "hi")

# text to speech.
target_audio = gTTS(target_text)
target_audio.save("target_audio.mp3")
