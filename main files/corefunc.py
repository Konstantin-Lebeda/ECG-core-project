# collection of all requirement functionns

# improts
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.fftpack as fftpack
import statsmodels.api as sm
from sqlalchemy import column
from scipy.fft import fft, fftfreq

# data frame read from CSV
# takes filename, returns pandas dataframe
def DFReadCSV(filename):
    df = pd.read_csv(filename, encoding='unicode_escape', header=None)
    df.columns = ['time', 'voltage', 'shit']

    return df

# extracting colomns 'time' and 'voltahe' from df
# takes pandas dataframe, returns lists of time and voltage
def DFExtractData(df):
    time, voltage = [], []
    for i in range(len(df)):
        time.append(df.loc[i, 'time'])
        voltage.append(df.loc[i, 'voltage'])
    
    return time, voltage

# lowess
# takes x and y, returns lowess(y)
def LowessSig(x, y):
    lowess = sm.nonparametric.lowess
    
    return lowess(exog=x, endog=y, frac=0.005, return_sorted=False)

# fast Fourier transformation
# takes y data and data collecting frequency, returns x and y of transformation
def FFTSig(y, freq):
    t = np.arange(len(y))
    v = np.array(y)
    
    return np.fft.fftfreq(t.size, 1/(freq * 10**6)), np.abs(np.fft.fft(v * (2 * np.pi)))

