import os
from pytube import YouTube #pytube currently has a bug with captions. https://github.com/pytube/pytube/pull/1388 to fix it
import subprocess
import warnings

class Downloader:
    def __init__(self, link:str, title:str, save_dir:str = ''):
        self.link = link
        self.title = title.replace(' ', '_').replace('\"','').replace('\'','').replace('|','').replace('/','')
        self.save_dir = save_dir

    def download(self):
        yt = YouTube(self.link)
        yv = yt.streams.filter(only_video=True, adaptive=True, file_extension='mp4').order_by('resolution').desc().first() #video stream with highest resolution
        ya = yt.streams.filter(only_audio=True).order_by('abr').desc().first() #audio stream with highest resolutions
        path = os.path.join(self.save_dir, self.title)
        
        #download subtitles
        yc = get_caption_by_language_name(yt, 'English')
        if yc == None:
            yc = get_caption_by_language_name(yt, 'English (auto-generated)')
            if yc == None:
                print('No captions found for video: ' + self.title)
        try:
            yc.download(output_path = path, title = self.title + '.srt', srt=True)
        except:
             warnings.warn('Error downloading captions for video: ' + self.title)
             return 
            
        #download video
        yv.download(output_path = path, filename = self.title + '.mp4')
        
        #download audio, convert to wav
        ya.download(output_path = path, filename = self.title + '.webm')
        audio_path = os.path.join(path, self.title)
        webm2wav(audio_path)
                    
def get_caption_by_language_name(yt, lang_name):
	for caption in yt.caption_tracks:
		if caption.name == lang_name:
			return caption
        
def webm2wav(audio_path):
    command = f"ffmpeg -i {audio_path}.webm -ab 160k -ac 2 -ar 44100 -vn {audio_path}.wav"
    
    subprocess.call(command, shell=True)
    
    os.remove(audio_path + '.webm')
    