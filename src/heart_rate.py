import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt
import pandas as pd

# ----------------------
# Generate synthetic ECG-like signal
# ----------------------
fs = 250  # sampling frequency
t = np.linspace(0, 10, fs * 10)  # 10 seconds
signal = 1.5 * np.sin(2 * np.pi * 1.2 * t)  # base wave
noise = 0.3 * np.random.randn(len(t))
ecg = signal + noise

# ----------------------
# Filter the signal
# ----------------------
b, a = butter(3, 0.05)
filtered_ecg = filtfilt(b, a, ecg)

# ----------------------
# Peak Detection
# ----------------------
peaks, _ = find_peaks(filtered_ecg, height=0.5, distance=fs*0.4)
bpm = (len(peaks) / (len(t) / fs)) * 60

print(f"Estimated Heart Rate: {bpm:.2f} BPM")

# ----------------------
# Save data
# ----------------------
df = pd.DataFrame({"time": t, "ecg_signal": ecg})
df.to_csv("../data/example_signal.csv", index=False)

# ----------------------
# Plot
# ----------------------
plt.plot(t, filtered_ecg)
plt.scatter(t[peaks], filtered_ecg[peaks], color='red')
plt.title("Synthetic ECG Signal with Detected Peaks")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
