from .downloader import Downloader
from .scraper import get_video_results

class yt_dl:
    def __init__(self, query:str, num_videos:int, save_dir:str = ''):
        self.query = query
        self.num_videos = num_videos
        self.video_results = get_video_results(self.query, self.num_videos)
        self.save_dir = save_dir

    def download(self):
        for result in self.video_results:
            Downloader(result['link'], result['title'], save_dir=self.save_dir).download()