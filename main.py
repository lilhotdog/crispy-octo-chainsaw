import mido
from mido  import MidiFile, MetaMessage

mid = MidiFile('Queen - Bohemian Rhapsody.mid', clip=True)
new_midi = MidiFile()

banned = ('drum', 'hit', 'timpani') # Instruments we don't want

for track in mid.tracks:
    if track[0].type == 'text':
        track_name = track[0].text # Get the name of the track
        not_banned = all(ban not in track_name.lower() for ban in banned) # Make sure the track isn't banned
        if not_banned:
            print(track_name)
            track[0] = MetaMessage('text', text='Piano') # Change the track name to Piano
            new_midi.tracks.append(track) # Add the track to the new midi
        else:
           print('Banished track: ', track_name) # Remove percussion
    else:            
        new_midi.tracks.append(track) # Add any track that's not an instrument

new_midi.save('test.mid')