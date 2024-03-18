import numpy as np
import scipy.io as sio
import scipy.io.wavfile
from scipy import fftpack

samplerate, data = sio.wavfile.read('test.wav')
fftsize = len(data)
data_fft = fftpack.fft(data, fftsize)

# fast fourier transform 
