import numpy as np
import glob
import os
import nltk
import pronouncing
from tqdm import tqdm

class rhymer():
    def __init__(self, srts_dir:str):
        self.videos, self.scripts = self.load_srts(srts_dir)
        self.words, self.lookup = self.get_words() # get all words to rhyme with
        self.rhyme_matrix = self.rhyme_matrix()
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
                        cap_set = [begin, end, text] #misses the last line
                        script.append(cap_set)
                scripts.append(script)
        return videos, scripts
    def get_words(self):
        """Take the scripts, pull out the relevant words from each script, and return a list of all words in one object"""
        words = []
        lookup = []
        for i,script in enumerate(self.scripts):
            video = self.videos[i]
            for cap_set in script:
                start = cap_set[0]
                stop = cap_set[1]
                text = cap_set[2]
                phrase = text.split(' ')
                for word in phrase:
                    lookup.append((video,start,stop))
                words.extend(phrase)
        return np.array(words), np.array(lookup)
        
    def rhyme_matrix(self):
        num_words = len(self.words)
        rhy_mat = np.zeros((num_words,num_words))
        for x,row in enumerate(tqdm(rhy_mat)): # iterate over rows
            rhymingwords = pronouncing.rhymes(self.words[x]) # get rhyming words
            for y,word in enumerate(self.words[x:]): # iterate over valid columns
                if word in rhymingwords:
                    rhy_mat[x,y+x] = 1 #triangular matrix 
        return rhy_mat
    
    def get_rhymes(self):
        """Returns a list of rhymes with their corresponding time stamps"""
        x,y = np.where(self.rhyme_matrix == 1)
        rhymes = [self.words[x],self.words[y],self.lookup[x],self.lookup[y]]
        return rhymes
        
rh = rhymer('/home/tony/github/videorhyme/videos')
print(rh.get_rhymes())