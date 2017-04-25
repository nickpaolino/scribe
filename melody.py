import random
import json
from music21 import *
import music21

class Melody(object):
    notes = "C C# D D# E F F# G G# A A# B".split() * 2
    with open('/Users/nicholaspaolino/github/scribe/Data/scales.json') as f:
        scales = json.load(f)
    def __init__(self):
        return None
    def generate_melody(self, number, scale_type, key):
        self.number = number
        self.scale_type = scale_type
        self.key = key
        melody = stream.Stream()
        h, w, m = 1, 2, 3 # Define intervals
        key_range = Melody.notes[Melody.notes.index(key):Melody.notes.index(key) + 12]
        scale = [eval(x) for x in Melody.scales[scale_type].split()] # reads scale type from json file
        flatten = lambda l: [item for sublist in l for item in sublist]
        scale_vector = flatten([range(x) for x in scale])
        scale_type = [x for x, y in zip(key_range, scale_vector) if y == 0]
        scale = [random.choice(scale_type) + random.choice(["4","5"]) for n in [0]*number] # Octave 3 is the middle octave
        random.shuffle(scale)
        melody.append([note.Note(x, type = self.generate_rhythm()) for x in scale])
        return melody
    def generate_rhythm(self):
        rhythmic_units = ['whole','half','quarter','eighth'] # Define basic rhythmic units
        return random.choice(rhythmic_units)
    def interpret_stream(self, stream):
        notes, rhythm = [], []
        notes = [note for note in stream if type(note) == music21.note.Note]
        rhythm = [beat.duration.quarterLength for beat in stream if beat.duration.quarterLength != 0]
        return zip(notes, rhythm) # Returns a tuple with the note type object and the rhythmic duration in quarter notes
