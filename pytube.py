#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Jangan di recode ya bossque, masa bikin tools seperti ini aja anda gak mampu?!. ;)

from __future__ import unicode_literals
import os
import sys
import time
import youtube_dl

os.system("clear")
logo = ('''\033[0m
 ._______.       ._______.       .__.
 |   _   |.--.--.|       |.--.--.|  |--..-----.
 |.  1   ||  |  ||.|   | ||  |  ||  _  ||  -__|
 |.  ____||___  |`-|.  |-'|_____||_____||_____|
 |:  |    |_____|  |:  | Author : ITermSec
 |::.|\033[0m Version\033[32m 1.3\033[0m |::.| https://github.com/ITermSec
 `---'             `---' https://instagram.com/itermsec_
   (Download Video & Audio using python3.7.3)''')
menu = ('''\033[0m
  [\033[32m01\033[0m]\033[1;37m Audio Download\033[0m  [\033[32m00\033[0m]\033[1;31m Exit\033[0m
  [\033[32m02\033[0m]\033[1;37m Video Download\033[0m  [\033[32m99\033[0m]\033[1;32m Information\033[0m
''')
print(logo)
print(menu)

def ext():
	con=input('    \033[0mContinue??? [\033[32mY\033[1;30m/\033[0m\033[31mn\033[0m]\033[1;30m :\033[0m ')
	if con[0].upper() == 'N':
		os.system("clear")
		print("\t\t\033[0m       Good Bye!!!")
		os.system("sleep 2")
		os.system("clear")
		exit()
	else:
		os.system("clear")
		print(logo)
		print(menu)
		select()

def select():
    try:
        choose=input("\033[0m[\033[31m?\033[0m] Choose\033[1;30m :\033[0m ")
        if choose == '2' or choose == '02':
            os.system("clear")
            print("""\033[0m
\t\t .___ ___,       .___ ___,
\t\t |   Y   |.-----.|   Y   |
\t\t |.      ||  _  ||   |   |
\t\t |. \_/  ||   __||____   |
\t\t |:  |   ||__|       |:  |
\t\t |::.|:. |           |::.|
\t\t `--- ---'           `---'
""")
            ydl_opts = {}
            os.chdir('Download/')
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            	ydl.download([input('\033[0m[\033[1;31m!\033[0m] URL\033[1;30m :\033[0m ')])
            print("")
            ext()
        elif choose == '1' or choose == '01':
            os.system("clear")
            print("""\033[0m
\t\t .___ ___.       ._______,
\t\t |   Y   |.-----.|   _   |
\t\t |.      ||  _  ||___|   |
\t\t |. \_/  ||   __| _(__   |
\t\t |:  |   ||__|   |:  1   |
\t\t |::.|:. |       |::.. . |
\t\t `--- ---'       `-------'
""")
            ydl_opts = {
                'format': 'bestaudio/best',
                'extractaudio':True,
                'outtmpl':'Download/%(title)s.%(id)s', 
                'nocheckcertificate': True,
                'playlist':True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([input('\033[0m[\033[1;31m!\033[0m] URL\033[1;30m :\033[0m ')])
            ext()
        elif choose == '99':
            os.system("clear")
            print(logo)
            print('')
            print(" Information :")
            print("\033[0m [\033[1;30m#\033[0m] Download Video & Audio using python3.7.3")
            print("\033[0m [\033[1;30m#\033[0m] Version 1.3")
            print("\033[0m [\033[1;30m#\033[0m] Author\033[1;30m :\033[0m\033[32m ITermSec")
            print("\033[0m [\033[1;30m#\033[0m] Thanks To\033[1;30m :\033[0m\033[32m DedSecTL")
            print("\033[0m [\033[1;30m#\033[0m] GitHub\033[1;30m :\033[0m\033[32m https://github.com/ITermSec")
            print("\033[0m [\033[1;30m#\033[0m] Instagram\033[1;30m :\033[0m\033[32m https://instagram.com/itermsec_")
            print("\033[0m [\033[1;30m#\033[0m]\033[0m Date\033[1;30m :\033[0m Monday, 24-06-2019 (01:26)")
            print("\033[0m [\033[1;30m#\033[0m]\033[0m Team\033[1;30m :\033[1;37m BlackHole Security\033[0m")
            print("            \033[1;32mSurabaya Black Hat\033[0m")
            print("            \033[1;34mLCT\033[0m")
            print("            \033[1;31mCRABS\033[0m")
            ext()
        elif choose == '00':
            print("\t\t       Good Bye!!!")
            quit()
    except KeyboardInterrupt:
        os.system("clear")
        print("\t\t       Good Bye!!!")
        quit()

try:
  os.mkdir('Download')
except OSError:
  pass

if __name__ == "__main__":
  select()
