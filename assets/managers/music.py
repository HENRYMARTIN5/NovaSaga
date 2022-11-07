from assets.util.logging import *
from pygame import mixer
import os


class MusicManager:
    def __init__(self):
        mixer.init()
        self.music = {}
        self.current_music = None
        self.current_track = None
        self.fetch_music("assets/music")

    def fetch_music(self, dir):
        info("Fetching music from " + dir)
        for file in os.listdir(dir):
            if file.endswith(".wav"):
                self.music[file] = os.path.join(dir, file)
                debug("Found music file " + file)
    
    def play(self, name):
        if name + ".wav" in self.music:
            if self.current_music and self.current_track != name:
                self.current_music.stop()
                self.current_music.fadeout(1500)
            elif self.current_track == name:
                debug("Music " + name + " is already playing, ignoring request")
                return
            
            self.current_music = mixer.Sound(self.music[name + ".wav"])
            self.current_music.play()
            debug("Playing music " + name)
        else:
            error("Music file " + name + ".wav not found")
    
    def stop(self):
        if self.current_music:
            self.current_music.stop()
            self.current_music = None
    
    def pause(self):
        if self.current_music:
            self.current_music.stop()

    def unpause(self):
        if self.current_music:
            self.current_music.play()
    
    def get_current_music(self):
        return self.current_music