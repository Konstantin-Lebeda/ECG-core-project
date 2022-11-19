print('-' *25)
print('simpletest STARTED')
import numpy
import matplotlib
import matplotlib.pyplot as plt
import pandas
import scipy
import statsmodels
import sqlalchemy
print('... requirements OK')
import corefunc as cf
print('... corefunc OK')
df = cf.DFReadCSV('EXAMPLE.CSV')
print('... DFReadCSV OK')
time, voltage = cf.DFExtractData(df)
print('... DFExtractData OK')
sig = cf.LowessSig(time, voltage)
print('... LowessSig OK')
freq, fft = cf.FFTSig(sig, 0.002)
print('... FFTSig OK')

plt.figure(figsize=(16,8))

plt.subplot(3, 2, 1)
plt.plot(time, voltage, linewidth=1, color='black')
plt.grid(color='black', linewidth=0.5)
plt.ylabel("Signal")

plt.subplot(3, 2, 3)
plt.plot(time, voltage, linewidth=1, color='black')
plt.plot(time, sig, linewidth=2, color='red')
plt.grid(color='black', linewidth=0.5)
plt.ylabel("Signal+lowess")

plt.subplot(3, 2, 5)
plt.plot(time, sig, linewidth=2, color='green')
plt.grid(color='black', linewidth=0.5)
plt.ylabel("lowess")

plt.subplot(1, 2, 2)
plt.plot(freq, fft, linewidth=2, color='blue')
plt.grid(color='black', linewidth=0.5)
plt.xlim(-60, 60)
plt.title("FFT of signal after lowess")

plt.tight_layout(h_pad=2)
plt.tight_layout(w_pad=2)

plt.show()

print('simpletest COMPLETE, have fun!')
print('-' *25)