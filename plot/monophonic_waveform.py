# Plot a monophonic waveform
import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
plt.figure()
plt.subplot(3, 1, 1)
librosa.display.waveplot(y, sr=sr)
plt.title('Monophonic')
plt.tight_layout()
plt.show()