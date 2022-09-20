# from videorhyme.yt_dl import VideoRhyme
from videorhyme.youtube_dl.yt_dl import yt_dl

downloader = yt_dl(query = 'protest', num_videos = 5, save_dir='videos')
downloader.download()

# vr = VideoRhyme('presidential speech', num_videos=10)
