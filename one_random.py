__author__ = 'lukestack'

#!/usr/bin/env python
# encoding: utf=8
"""
one_random.py

For each beat in the song, replace it with a different random beat that has the same local_context.
It also plays as it runs using aqplayer instead of creating a new file.

one.py #original
By Ben Lacker, 2009-02-18. #original author
"""
import echonest.remix.audio as audio
from aqplayer import Player
import random

usage = """
Usage:
    python one.py <input_filename>

Example:
    python one.py EverythingIsOnTheOne.mp3 
"""

def main(input_filename):
    audiofile = audio.LocalAudioFile(input_filename)
    player = Player(audiofile)
    bars = audiofile.analysis.bars
    collect = audio.AudioQuantumList()
    for i in range(len(bars)):
        for j in range(len(bars.__getitem__(i).children())):
            rint = random.randint(0, len(bars) - 1)
            if len(bars.__getitem__(rint).children()) >= j:
                beat = bars.__getitem__(rint)
            else:
                beat = bars.__getitem__(rint).children()[0]
            player.play(beat, False)
    player.close()

if __name__ == '__main__':
    import sys
    try:
        input_filename = sys.argv[1]
    except:
        print usage
        sys.exit(-1)
    main(input_filename)