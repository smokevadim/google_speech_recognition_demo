#!/usr/bin/env python3
import speech_recognition as sr


# obtain path to "english.wav" in the same folder as this script
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio\\FM935M_20181122_0530_m2.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Google Cloud Speech
with open('google_credentials.json', 'r', encoding='utf-8') as fh:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = fh.read()
try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, language='es-CR', credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))