from __future__ import print_function
import librosa

# 1. Get the file path to the included audio example
filename = librosa.util.example_audio_file()

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load("a2002011001-e02-128k.ogg")

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# audio Sample from - music.helsinki.fi
# http://www.music.helsinki.fi/tmt/opetus/uusmedia/esim/index-e.html

# output for input - 2002011001-e02-32k.ogg
# Estimated tempo: 83.35 beats per minute

# output for input - a2002011001-e02-128k.ogg
# Estimated tempo: 161.50 beats per minute