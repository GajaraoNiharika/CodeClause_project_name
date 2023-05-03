import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")

        self.playlist = []
        self.current_index = 0
        self.playing = False

        self.create_widgets()

        pygame.init()
        pygame.mixer.init()

    def create_widgets(self):
        # Create buttons
        self.button_add = tk.Button(self.master, text="Add", command=self.add_song)
        self.button_play = tk.Button(self.master, text="Play", command=self.play_song)
        self.button_stop = tk.Button(self.master, text="Stop", command=self.stop_song)
        self.button_prev = tk.Button(self.master, text="<<", command=self.prev_song)
        self.button_next = tk.Button(self.master, text=">>", command=self.next_song)

        # Create playlist box
        self.playlist_box = tk.Listbox(self.master, width=50)
        self.playlist_box.bind("<Double-Button-1>", self.play_song)

        # Add buttons and playlist box to window
        self.button_add.pack(pady=5)
        self.button_play.pack(side=tk.LEFT, padx=5)
        self.button_stop.pack(side=tk.LEFT, padx=5)
        self.button_prev.pack(side=tk.LEFT, padx=5)
        self.button_next.pack(side=tk.LEFT, padx=5)
        self.playlist_box.pack(pady=5)

    def add_song(self):
        songs = filedialog.askopenfilenames(title="Select Songs", filetypes=[("Ed_Sheeran_-_Perfect_NaijaMusic.Ng.mp3", "[iSongs.info] 07 - Happy Days.mp3",)])
        if songs:
            for song in songs:
                self.playlist.append(song)
                self.playlist_box.insert(tk.END, os.path.basename(song))

    def play_song(self, event=None):
        if not self.playing and self.playlist:
            song = self.playlist[self.current_index]
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.playing = True

    def stop_song(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

    def prev_song(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.stop_song()
            self.play_song()

    def next_song(self):
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.stop_song()
            self.play_song()

    def play_playlist(self):
        if not self.playing and self.playlist:
            song = self.playlist[self.current_index]
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.playing = True
            self.current_index += 1
            if self.current_index >= len(self.playlist):
                self.current_index = 0
        self.master.after(1000, self.play_playlist)

root = tk.Tk()
music_player = MusicPlayer(root)
music_player.play_playlist()
root.mainloop()
