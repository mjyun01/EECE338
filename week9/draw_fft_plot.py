import numpy as np
import scipy.io as sio
import scipy.io.wavfile
from scipy import fftpack

samplerate, data = sio.wavfile.read('test.wav') # YOU CAN CHANGE 'test.wav' TO YOUR OWN FILENAME
fftsize = len(data) 
data_fft = fftpack.fft(data, fftsize)

Ts = 1/samplerate 
############################################
# WRITE DOWN YOUR FFT PLOT CODE HERE 
# X axis is Frequency, Y axis is Power



############################################

plt.show()
