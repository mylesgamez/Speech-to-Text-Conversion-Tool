# Speech to Text Conversion using Python
This project uses the SpeechRecognition and pydub Python libraries to convert audio files into text. It's a command-line script that accepts an audio file and prints the transcription.

## Installation
Make sure you have the following Python packages installed:
SpeechRecognition
pydub

You can install them with pip:
``` pip install SpeechRecognition pydub ```

## Usage
To transcribe an audio file, run the script from the command line:
``` python speech_to_text.py path_to_your_audio_file.mp3 ```

The script will print the transcription of the audio file.

## Disclaimer
This script uses the free tier of the Google Speech Recognition API, which is not intended for heavy use. If you plan to use this script regularly, consider setting up a paid API.

Also, please note that the accuracy of the transcription depends on the quality of the audio file and the clarity of the speech.

## License
This project is released under the MIT License.



