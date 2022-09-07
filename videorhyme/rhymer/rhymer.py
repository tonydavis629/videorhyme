import numpy as np
import glob
import os

class rhymer():
    def __init__(self, srts_dir:str):
        self.videos, self.scripts = self.load_srts(srts_dir)
    def load_srts(self, srts_dir:str):
        #find the paths of the srt files
        # srt_paths = glob.glob(srts_dir + '/*/*.srt')
        videos = os.listdir(srts_dir)
        srt_paths = []
        for video in videos:
            # find the paths of the srt files
            srt = glob.glob(srts_dir + '/' + video + '/*.srt')
            srt_paths.extend(srt)
            
        scripts = []      
        for path in srt_paths:
            with open(path, 'r') as f:
                script = []
                # read individual lines
                for i, line in enumerate(f.readlines()):
                    # line type repeats every 4th line. 0 is line number and 3 is empty so skip those.
                    if i % 4 == 1:  # get time stamps
                        time_stamps = line.replace('\n', '').split(' --> ')
                        begin = time_stamps[0]
                        end = time_stamps[1]
                    elif i % 4 == 2:  # get text
                        text = line.replace('\n', '')[1:] #remove leading space
                    if i % 4 == 3: # append to script
                        cap_set = [begin, end, text]
                        script.append(cap_set)
                scripts.append(script)
        return videos, scripts
        
rh = rhymer('/home/tony/github/videorhyme/videos')
rh.videos
rh.scripts