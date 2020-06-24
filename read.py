import scipy
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

input_ = read("output.wav")
audio = input_[1]
plt.plot(audio[0:1048576])
plt.ylabel("dummyx")
plt.xlabel("dummyy")
plt.title("dummytitle")
plt.show()
