import numpy as np
import glob
import os
import nltk

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
                    if i % 4 == 3: # append to script
                        cap_set = [begin, end, text]
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
                    lookup.extend((video,start,stop))
                words.extend(phrase)
        return words, lookup
    
    def rhyme(self, inp, level):
        entries = nltk.corpus.cmudict.entries()
        syllables = [(word, syl) for word, syl in entries if word == inp]
        rhymes = []
        for (word, syllable) in syllables:
                rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
        return set(rhymes)
    
    def rhymescore(self,word1:str,word2:str):
        """Takes in two words and rates how well they rhyme"""
        if word1.find(word2) == len(word1) - len(word2):
            return False
        if word2.find(word1) == len(word2) - len(word1): 
            return False
        return word1 in self.rhyme(word2, 1)
        
    def rhyme_matrix(self):
        num_words = sum([len(i) for i in self.words])
        rhy_mat = np.zeros((num_words,num_words))
        for x,row in enumerate(rhy_mat):
            for y,val in enumerate(row):
                rhy_mat[x,y] = self.rhymescore(self.words(x),self.words(y))
                
        return rhy_mat
        
rh = rhymer('/home/tony/github/videorhyme/videos')
print(rh.rhyme_matrix())