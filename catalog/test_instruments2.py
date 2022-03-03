from EasyMIDI import *
from .mas_chord import *
from random import *


def test5_chord_def(name="noname"):
    temps = randint(120, 200)
    instrument = choice(instruments)
    major_minor = choice([False, True])
    mid = EasyMIDI()
    track = Track(instrument, temps)
    #String Ensemble 2

    notes_x = choice(chords_box)
    notes_generate_patern = []
    for i in range(60):
            notes_generate_patern.append(notes_x)
            notes_x = choice(patern_classic[notes_x])





    notes_generate_patern *= 2
    key_notes = choice(notes[:-1])
    for numeral in notes_generate_patern:
       track.addChord(RomanChord(numeral, major=major_minor, key=key_notes, octave=3)
    mid.addTrack(track)
    mid.writeMIDI(name)
    return instrument



