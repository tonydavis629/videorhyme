# from videorhyme.yt_dl import VideoRhyme
from videorhyme.youtube_dl.yt_dl import yt_dl

downloader = yt_dl(query = 'protest', num_videos = 3, save_dir='videos')
downloader.download()

# vr = VideoRhyme('presidential speech', num_videos=10)
# rm = vr.rhymematrix() # [n x n] triangle binary matrix of rhyming words in form (video,word_n,word)
# rhymes = vr.rhymes() # [{'id':str, 'video1':str, 'time1':float, 'word1':str, 'video2;str, 'time2':float, 'word2':str}, ...]
# videos = vr.videos(ids=rhymes[0:3].ids, window=5) # [{'video1':str, 'time1_i':float, time1f':float, 'video2':str, 'time2_i':float, 'time2_f':float}, ...]
# audio = vr.audio(ids=rhymes[0:3].ids, window=5) # [{'video1':str, 'time1_i':float, time1f':float, 'video2':str, 'time2_i':float, 'time2_f':float}, ...]
