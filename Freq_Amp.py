"""
Abstract : Librosa is a package which serves to study audio files
with the help of this package we'll load a function that will read in the path to an audio file, 
using two functions call .amplitude and .stft with the help of matplotlib package 
to mash up frequency and amplitude into a resulting array ploted graph
(NOTE : The default sampling rate used by Librosa is 22050, but I used 44100 due to the sample's lenght)
"""
import librosa
import numpy as np
import matplotlib.pyplot as plt

# Wav file path 

fichier = (r"C:\Users\Adam\Desktop\audio.wav") 
y, sr = librosa.load(fichier, sr=44100)

# Size of the fft 

n_fft = 2048 
S = librosa.stft(y, n_fft=n_fft, hop_length=n_fft//2) 
"""
hop_length : The number of samples between successive frames
n_fft and hop length determine frequency in function of time resolution converted to dB
""" 
D = librosa.amplitude_to_db(np.abs(S), ref=np.max)

# Calculate average over file

D_AVG = np.mean(D, axis=1) 
plt.bar(np.arange(D_AVG.shape[0]), D_AVG)
"""
Geometric representation of the Amplitude (dB) in fct of Frenquency (Hz)
 """ 
x_ticks_positions = [n for n in range(0, n_fft // 2, n_fft // 16)]
x_ticks_labels = [str(sr / 2048 * n) + 'Hz' for n in x_ticks_positions]
plt.xticks(x_ticks_positions, x_ticks_labels)
plt.xlabel('Fréquence')
plt.ylabel('Amplitude en dB')

# showing final result (graph) 

plt.show() 
