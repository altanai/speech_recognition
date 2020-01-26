# Librosa
music and audio analysis

## Components 

### librosa.beat
Functions for estimating tempo and detecting beat events.

### librosa.core
Core functionality includes functions to load audio from disk, compute various spectrogram representations, and a variety of commonly used tools for music analysis. For convenience, all functionality in this submodule is directly accessible from the top-level librosa.* namespace.

### librosa.decompose
Functions for harmonic-percussive source separation (HPSS) and generic spectrogram decomposition using matrix decomposition methods implemented in scikit-learn.

### librosa.display
Visualization and display routines using matplotlib.

**specshow** - Display a spectrogram/chromagram/cqt/etc.
librosa.display.specshow(data, x_coords=None, y_coords=None, x_axis=None, y_axis=None, sr=22050, hop_length=512, fmin=None, fmax=None, tuning=0.0, bins_per_octave=12, ax=None, **kwargs)

**librosa.display.waveplot** - Plot the amplitude envelope of a waveform.
librosa.display.waveplot(y, sr=22050, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000, ax=None, **kwargs)

### librosa.effects
Time-domain audio processing, such as pitch shifting and time stretching. This submodule also provides time-domain wrappers for the decompose submodule.

### librosa.feature
Feature extraction and manipulation. This includes low-level feature extraction, such as chromagrams, pseudo-constant-Q (log-frequency) transforms, Mel spectrogram, MFCC, and tuning estimation. Also provided are feature manipulation methods, such as delta features, memory embedding, and event-synchronous feature alignment.

### librosa.filters
Filter-bank generation (chroma, pseudo-CQT, CQT, etc.). These are primarily internal functions used by other parts of librosa.

### librosa.onset
Onset detection and onset strength computation.

### librosa.output
Text- and wav-file output. (Deprecated)

### librosa.segment
Functions useful for structural segmentation, such as recurrence matrix construction, time-lag representation, and sequentially constrained clustering.

### librosa.sequence
Functions for sequential modeling. Various forms of Viterbi decoding, and helper functions for constructing transition matrices.

### librosa.util
Helper utilities (normalization, padding, centering, etc.)

## Installation 

```bash
 pip3 install librosa
```

## Run

```bash
 python3 beat_tracking.py
```
