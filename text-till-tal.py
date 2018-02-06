#!/usr/bin/env python3

from gtts import gTTS
import os
import sys


lang = 'sv'
text = ' '.join(sys.argv[1:])
tts = gTTS(text=text, lang=lang)
tts.save('snd.mp3')
os.system('mplayer snd.mp3')
