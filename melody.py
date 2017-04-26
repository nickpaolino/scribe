import json
import random
import music21
from music21 import *

def read_scale(scale_type, key):
    # Notes are in string format and read from Music21's library
    notes = "C C# D D# E F F# G G# A A# B".split() * 2

    # Define intervals: half step, whole step, minor third
    h, w, m = 1, 2, 3

    # Reads scale from json file that defines the scale's succession of intervals
    with open('/Users/nicholaspaolino/github/scribe/Data/scales.json') as f:
        scales = json.load(f)

    # The key range is the chromatic range starting at the key note
    key_range = notes[notes.index(key):notes.index(key) + 12]

    # Evaluates the intervals, listed as strings in the json, into variables
    scale = [eval(x) for x in scales[scale_type].split()]

    # Defines lambda function to flatten list, removing the notes that are not part of the key and scale range
    flatten = lambda l: [item for sublist in l for item in sublist]
    scale_vector = flatten([range(x) for x in scale])

    # Returns the notes of the scale as strings in list form
    return [x for x, y in zip(key_range, scale_vector) if y == 0]

def generate_melody(number):
    melody = stream.Stream() # Define music21 stream

    # Creates a list of the requested amount of random notes from the scale - variables currently set default
    scale_material = [random.choice(read_scale("pentatonic","A")) + random.choice(["4","5"]) for n in [0]*number]

    # Shuffles the randomized notes
    random.shuffle(scale_material)

    # Creates the melody by appending the random sequence of notes it to the music21 stream
    melody.append([note.Note(x, type = generate_rhythm()) for x in scale])
    return melody

def generate_rhythm():
    # Defines basic rhythmic units through the music21 library
    rhythmic_units = ['whole','half','quarter','eighth']
    return random.choice(rhythmic_units)

def interpret_stream(stream):
    notes, rhythm = [], []

    # Creates a list of the music21 note objects
    notes = [note for note in stream if type(note) == music21.note.Note]

    # Creates a list of the music21 note duration types
    rhythm = [beat.duration.quarterLength for beat in stream if beat.duration.quarterLength != 0]

    # Returns a tuple with the note type object and the rhythmic duration in quarter notes
    return zip(notes, rhythm)
def write_midi(stream):

    # Writes midi file to save the melody
    mf = midi.translate.streamToMidiFile(stream)
    mf.open('/Melody'+'/midi'+str(random.randint(1, 1000))+'.mid','wb')
    mf.write()
    mf.close()
