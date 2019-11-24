# This python script preforms an MFCC analysis of every .wav file into a matrix representation output
# Requires python_speech_features. 
# Requires scipy. 
# import things we're going to need
 
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav

# import of wav file

(rate,sig) = wav.read(r"C:\Users\Adam\Desktop\125BOUNC-mono.wav")

# get mfcc

mfcc_feat = mfcc(sig,rate)

# get filterbank energies

fbank_feat = logfbank(sig,rate)

# showing results

print(fbank_feat[1:3,:])