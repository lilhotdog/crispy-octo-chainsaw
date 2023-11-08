from mido  import MidiFile

mid = MidiFile('Queen - Bohemian Rhapsody.mid', clip=True)
new_midi = MidiFile()

banned = ('drum', 'hit', 'timpani', 'perc') # Instruments we don't want


for track in mid.tracks: # Loop through all of the tracks in the midi file
    if track[0].type == 'text':
        track_name = track[0].text # Get the name of the track
        not_banned = all(ban not in track_name.lower() for ban in banned) # Make sure the track isn't banned
        if not_banned:
            for msg in track:
                if not msg.is_meta:
                    msg.channel=0 # Set the midi channel to 0
            track[0].text='Piano' # Change the track name to Piano
            new_midi.tracks.append(track) # Add the track to the new midi
        else:
           print('Banished track: ', track_name) # Remove percussion
    else:            
        new_midi.tracks.append(track) # Add any track that's not an instrument (tempo track)

new_midi.save('test.mid')