from pytube import YouTube

import os

class Youtubed:
    def __init__(self, link):
        self.yt = YouTube(link)
        self.title = self.yt.title
        
    def download(self, type: str, quality='max'):
        if (type == 'mp4'):
            if (quality == 'max'):
                self.yt.streams.filter(progressive=True).order_by('resolution').desc().first().download(output_path="data", filename=f"{self.title}.mp4")
            else:
                self.yt.streams.filter(progressive=True).order_by('resolution').first().download(output_path="data", filename=f"{self.title}.mp4")
        elif (type == 'mp3'):
             self.yt.streams.filter(only_audio=True).first().download(output_path="data", filename=f'{self.title}.mp3')
             

             
    def clear():
        os.remove('data/video.mp3')
        os.remove('data/audio.mp3')