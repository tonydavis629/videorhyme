import os
from pytube import YouTube
import subprocess

class Downloader:
    def __init__(self, link:str, title:str, save_dir:str = ''):
        self.link = link
        self.title = title.replace(' ', '_').replace('\"','').replace('\'','')
        self.save_dir = save_dir

    def download(self):
        yt = YouTube(self.link)
        yv = yt.streams.filter(only_video=True, adaptive=True, file_extension='mp4').order_by('resolution').desc().first() #video stream with highest resolution
        ya = yt.streams.filter(only_audio=True, adaptive=True).order_by('abr').desc().first() #audio stream with highest resolutionself.titleself.title

        path = os.path.join(self.save_dir, self.title).replace(' ', '_').replace('\"','\'').replace('\'','')
        yv.download(output_path = path, filename = self.title + '.mp4')
        ya.download(output_path = path, filename = self.title + '.webm')
          
        audio_path = os.path.join(path, self.title)
        command = f"ffmpeg -i {audio_path}.webm -ab 160k -ac 2 -ar 44100 -vn {audio_path}.wav"
        
        subprocess.call(command, shell=True)
        
        os.remove(audio_path + '.webm')