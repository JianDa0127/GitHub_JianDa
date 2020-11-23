from pytube import YouTube
from moviepy.editor import VideoFileClip
# import time

# 把MP4轉成MP3
def video2sound(SongName,times):
    try:
        if times<3:
            video = VideoFileClip('{}.mp4'.format(SongName))
            video.audio.write_audiofile('{}.mp3'.format(SongName))
        else: # 轉失敗三次直接印出FAIL
            print('[Fail]Video to Sound : {}'.format(SongName))
    except:
        video2sound(SongName,times+1)

# 下載YT的影片
def Download(SongNameStrinig,ytID):
    try:
        url = YouTube('https://www.youtube.com/watch?v={}'.format(ytID))
        file=url.streams.filter().first()
        file.download(filename=SongNameStrinig)
        video2sound(SongNameStrinig,0)
    except:
        print('[Fail]Download : {}'.format(SongNameStrinig))
        Download(SongNameStrinig,ytID)
