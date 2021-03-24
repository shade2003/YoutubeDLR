#main.py

from pytube import YouTube

link = input("   Enter video's link ...\n   ")
try:
    video = YouTube(str(link))
except:
    print('     Something went wrong')
    print('     Check if your link is valid')
    exit('     Exiting app ...')

res = input('   Choose the number of the resolution you like!\n   0: 360p\n   1: 720p\n   2: 1080p\n   ')
options = [ '360p', '720p', '1080p' ]

try:
    chosen_stream = video.streams.filter(file_extension = 'mp4', resolution = options[int(res)])
except:
    print('This resolution is not available')
    exit('Exiting app ...')

download_stream = chosen_stream[0].download(r'C:\Users\shed2003\Videos\dw') #put in the destination/location of the final file.