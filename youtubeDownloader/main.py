from __future__ import unicode_literals
import youtube_dl

import sys

modulename = 'youtube_dl'
if modulename not in sys.modules:
    print('You have not imported the {} module'.format(modulename))
else:
    print("found")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}

mp3 = input("Enter your URL: ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([mp3])
