import os
from pytube import YouTube

class Downloader:
    def __init__(self, link:str, title:str, save_dir:str = ''):
        self.link = link
        self.title = title
        self.save_dir = save_dir

    def download(self):
        yt = YouTube(self.link)
        yv = yt.streams.filter(only_video=True, adaptive=True, file_extension='mp4').order_by('resolution').desc().first() #video stream with highest resolution
        ya = yt.streams.filter(only_audio=True, adaptive=True).order_by('abr').desc().first() #audio stream with highest resolutionself.titleself.title

        yv.download(os.path.join(self.save_dir, self.title))
        ya.download(os.path.join(self.save_dir, self.title))
