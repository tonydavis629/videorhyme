from pytube import YouTube


link = 'https://www.youtube.com/watch?v=D_79F_VWn0o'
yt = YouTube(link)
yv = yt.streams.filter(only_video=True, adaptive=True, file_extension='mp4').order_by('resolution').desc().first() #video stream with highest resolution
ya = yt.streams.filter(only_audio=True, adaptive=True).order_by('abr').desc().first() #audio stream with highest resolution

yv.download()
ya.download()
