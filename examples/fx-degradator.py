"""
fx-degradator.py - Signal quality degradator.

This example shows signal degradation effect with the
degradation factor and a lowpass filter cutoff controlled 
by analog inputs (use audio inputs after the stereo audio
channels, ie. Input(2) is analog-in 0, Input(3) is 
analog-in 1, etc.).

"""
# Set to True if you want to control the degradation
# and lowpass filter with analog inputs.
WITH_ANALOG_INPUT = True
# If False, set frequency and brightness values.
DEGRADATION = 0.75  # 0 -> 1
LPCUTOFF = 2500	    # (Hz)

# stereo input
src = Input([0,1])

if WITH_ANALOG_INPUT:
    # analog-in 0 (degradation)
    i1 = Input(2)
    # analog-in 1 (lowpass filter cutoff)
    i2 = Input(3)
    freq = (1.0 - i2) * 10000 + 50
else:
    i1 = DEGRADATION
    freq = LPCUTOFF

# Controllers scaling
invi1 = 1.0 - i1
bit = invi1 * 4.0 + 2.0
sr = invi1 * 0.48 + 0.02
sr2 = invi1 * 0.49 + 0.01

# DSP
deg = Degrade(src, bit, [sr,sr2])
lp = MoogLP(deg, freq, res=i1, mul=0.4).out()

