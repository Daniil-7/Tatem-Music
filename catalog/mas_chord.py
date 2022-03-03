from random import *


notes = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'R']

chords_box = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']


instruments = ['Acoustic Grand Piano', 'Bright Acoustic Piano',
 'Electric Grand Piano',
 'Electric Piano 2', 'Celesta',
 'Xylophone', 'Orchestra Hit', 'Shamisen',
 'Kalimba', 'Taiko Drum']
#Honky-tonk Piano

patern_classic = {
'I': ['II', 'III', 'IV', 'V', 'VI', 'VII'],
'II': ['I', 'III', 'V'],
'III': ['I','IV', 'V', 'VI', 'VII'],
'IV': ['I', 'II', 'V'],
'V': ['I', 'III', 'VI', 'VII'],
'VI': ['I', 'II', 'III', 'IV'],
'VII': ['I']
}


