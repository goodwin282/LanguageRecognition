# This is my initial exploratory code for our Capstone project
# The code has no direction, but will note what each step is doing as I explore

# We begin by reading in initial files from https://omniglot.com/soundfiles/
# I'll start by downloading the zip file for English (British) language, the file contains 156 voice recordings in mp3 format
# Install the necessary packages
import librosa
# PyAudio package is needed for capturing microphone input
import speech_recognition as sr
import ffmpeg
import pydub
import os
import glob

# First I installed ffmpeg on Windows following these instructions:
    # http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/

# Next I went to my directory and performed a command that loops through all mp3 files and turns them into .wav files
lst = glob.glob('C:\\Users\\Ryan G\\PycharmProjects\\LanguageRecognition\\AudioFiles\\britishenglishphrases\\*')

path = 'C:\\Users\\Ryan G\\PycharmProjects\\LanguageRecognition\\AudioFiles\\britishenglishphrases\\'

# Found out how to convert, now need to loop through whole directory and convert each one
# Create a function that will do this

# For now this works, need to figure a better way to rename the files
def mp3_to_wav(directory):
    for filename in directory:
        sound = pydub.AudioSegment.from_mp3(filename)
        sound.export(filename[:-4] + ".wav", format="wav")


# Run function on directory - currently british phrases 
mp3_to_wav(lst)