# This is my initial exploratory code for our Capstone project
# The code has no direction, but will note what each step is doing as I explore

# We begin by reading in initial files from https://omniglot.com/soundfiles/
# I'll start by downloading the zip file for English (British) language, the file contains 156 voice recordings in mp3 format
# Install the necessary packages
import librosa
# PyAudio package is needed for capturing microphone input
import os
import speech_recognition as sr
import ffmpeg
import pydub
import os
import glob

# First I installed ffmpeg on Windows following these instructions:
    # http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/

# Next I went to my directory and performed a command that loops through all mp3 files and turns them into .wav files
lst = glob.glob('C:\\Users\\Ryan G\\PycharmProjects\\LanguageRecognition\\AudioFiles\\britishenglishphrases\\*')

# Found out how to convert, now need to loop through whole directory and convert each one
# Create a function that will do this

# This function will loop through a directory and convert mp3 to wav so the SpeechRecognizer library will work on the files
# it then deletes the mp3 file
def mp3_to_wav(directory):
    for filename in directory:
        if filename[-3:] == 'mp3':
            sound = pydub.AudioSegment.from_mp3(filename)
            sound.export(filename[:-4] + ".wav", format="wav")
            os.remove(filename)


# Run function on directory - currently british phrases
mp3_to_wav(lst)

# The commented code below is a subset of the data I will use to try to find errors on the speech to text
"""
# convert the wav files from speech to text - practicing on subset of data
# let's find some errors in this after I try it with the full audio set
sub_lst = lst[0:9]

empty_lst = []
r = sr.Recognizer()

# append the audio from each audio file to the empty list 
for i in sub_lst:
    test = sr.AudioFile(i)
    with test as source:
        audio = r.record(source)
        empty_lst.append(audio)
        
# convert this audio to text and append it to a new list of phrases
inText = []
for audio in empty_lst:
    text = r.recognize_google(audio)
    inText.append(text)
"""

# Below I am running the above code on ALL the files, not going to error check, I will circle back to above code for this
store_audio = []
r = sr.Recognizer()

# append the audio from each audio file to the empty list
for i in lst:
    file = sr.AudioFile(i)
    with file as source:
        audio = r.record(source)
        store_audio.append(audio)

# convert this audio to text and append it to a new list of phrases
# Need an error catcher, if speech can not be recognized leave inText as NA
inText = []
for audio in store_audio:
    text = r.recognize_google(audio)
    inText.append(text)