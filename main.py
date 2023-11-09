from mido import MidiFile, MidiTrack, Message
import sys
import os

file = sys.argv[1] if len(sys.argv) > 1 else 'Queen - Bohemian Rhapsody.mid'
mid = MidiFile(file, clip=True)
new_midi = MidiFile()

banned_prog = (8, 9, 10, 11, 12, 13, 14, 15, 96, 97, 98, 99, 100, 101, 102, 103, 112, 113, 114, 115, 116, 118, 119) # Ban programs (FX, Percussion) ref https://jazz-soft.net/demo/GeneralMidi.html

# Create a dictionary to map channels to banned instruments
banned_channels = {}

for track in mid.tracks:
    new_track = MidiTrack()
    
    for msg in track:
        if not msg.is_meta:
            if hasattr(msg, 'program') and msg.program in banned_prog:
                # If a program change message is for a banned instrument, mark the channel as banned.
                banned_channels[msg.channel] = True
            if hasattr(msg, 'channel') and msg.channel not in banned_channels:
                msg.channel = 0
                # If the channel is not banned, add the message to the new track.
                new_track.append(msg)
    
    new_midi.tracks.append(new_track)

new_midi.save('new_' + os.path.basename(file))

print('File saved.')
