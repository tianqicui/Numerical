# Exercise 7.3
from numpy import loadtxt,arange,argmax,pi
from numpy.fft import rfft
from pylab import plot,show,figure,xlabel,ylabel,title

# Input rate and number of sample points
r = 44100
N = 100000
time = arange(0,N/r,1/r)

# Import data of piano
piano = loadtxt('piano.txt',float)
# Do fast Fourier transformation
cpiano = rfft(piano)
# Plot time-domain graph
figure(1)
xlabel("time/second")
ylabel("amplitude")
title("Time-domain of waveform of piano")
plot(time,piano)
# Plot frequency-domain graph
figure(2)
xlabel("order of coefficients")
ylabel("amplitude")
title("Frequency-domain of waveform of piano")
plot(abs(cpiano[:10000]))
# Find the main frequency
p = argmax(abs(cpiano[:10000]))
print("The piano plays with a frequency of",p*f/N,"Hz.")

# Similar method to deal with data of trumpet
trumpet = loadtxt('trumpet.txt',float)
ctrumpet = rfft(trumpet)
figure(3)
xlabel("time/second")
ylabel("amplitude")
title("Time-domain of waveform of trumpet")
plot(time,trumpet)
figure(4)
xlabel("order of coefficients")
ylabel("amplitude")
title("Frequency-domain of waveform of trumpet")
plot(abs(ctrumpet[:10000]))
t = argmax(abs(ctrumpet[:10000]))
print("The trumpet plays with a frequency of",t*f/N,"Hz.")
show()

#a)
# By comparing with two figures we could find that the sound of trumpet has a higher frequency and larger volume.

#b)
# We find that the piano and the trumpet play with a frequency of 524.79 Hz and 1043.847 Hz, respectively.
# So they are mainly playing C5 (freq = 523.25 Hz) and C6 (freq = 1046.5 Hz).