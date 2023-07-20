import speech_recognition as sr
from pydub import AudioSegment
import sys

def transcribe(file_path):
    # Load audio file
    audio = AudioSegment.from_file(file_path)

    # Convert to wav (required by the recognize_google function)
    audio = audio.export("temp.wav", format="wav")
    audio_path = "temp.wav"

    # Initialize recognizer
    r = sr.Recognizer()

    # open the file
    with sr.AudioFile(audio_path) as source:
        # read the entire audio file
        audio = r.record(source)

    # recognize speech using Google Speech Recognition
    try:
        print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    transcribe(sys.argv[1])
