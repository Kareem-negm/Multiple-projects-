from pytube import YouTube
from moviepy.editor import *
import os, shutil
from tkinter import *


#

      
def get_mp3():
    #make windos with tkinter
    windio=Tk()
    windio.geometry('500x300')
    windio.resizable(0,0)
    windio.title("Welcome to the youTube sound program  ")
    
    
    Label(windio, text ="Enter a YouTube link: "  ).place(x= 60,y=60) 
    Entry(windio, font = 'arial 10', textvariable = url, bg = 'ghost white').place(x=290, y = 60)
    Entry(windio, font = 'arial 10', textvariable = output, bg = 'ghost white').place(x=290, y = 80)


    
    url = input("Enter a YouTube link: ")
    output = input("What format would you like it in (wav/mp3)?: ")
    
    print("Converting...")

    mp4 = YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split(".mp4", 1)[0] + f".{output}"

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()

    os.remove(mp4)
    shutil.move(mp3, r"C:\Users\sample_user\Desktop")  # Replace this with your own output directory
    windio.mainloop()


get_mp3()