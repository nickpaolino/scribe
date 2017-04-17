import random
import json
from music21 import *

"""Add octaves, general length, note variation"""
class Melody(object):
    notes = "C C# D D# E F F# G G# A A# B".split() * 2
    with open('/Users/nicholaspaolino/Desktop/Scribe/Data/scales.json') as f:
        scales = json.load(f)
    def __init__(self):
        return None
    def generate_melody(self, number, scale_type, key):
        self.number = number
        self.scale_type = scale_type
        self.key = key
        melody = stream.Stream()
        melody.insert(0, instrument.PanFlute())
        melody.append(instrument.PanFlute())
        h, w, m = 1, 2, 3
        key_range = Melody.notes[Melody.notes.index(key):Melody.notes.index(key) + 12]
        scale = [eval(x) for x in Melody.scales[scale_type].split()] # reads scale type from json file
        flatten = lambda l: [item for sublist in l for item in sublist]
        scale_vector = flatten([range(x) for x in scale])
        scale_type = [x for x, y in zip(key_range, scale_vector) if y == 0]
        scale = [random.choice(scale_type) + "4" for n in [0]*number] # Octave 3 is the middle octave
        random.shuffle(scale)
        melody.append([note.Note(x, quarterLength = round(random.uniform(0.2, 2.0), 1)) for x in scale]) # Change decimal rounding to accommodate sheet music
        melody.show('midi')

a = Melody()
number = raw_input('number of notes: ')
scale_type = raw_input('scale: ')
key = raw_input('key: ')
a.generate_melody(int(number), scale_type, key)
