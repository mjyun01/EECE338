import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
samplerate, data = sio.wavfile.read('test.wav')
times = np.arange(len(data))/float(samplerate)		# (0:length(data)-1)/samplerate
plt.fill_between(times, data)		#fill the area between two horizontal curves(y=data and y=0) 
plt.xlim(times[0], times[-1])		#set x-axis limit
plt.xlabel('times (s)')
plt.ylabel('amplitude')
plt.show()
