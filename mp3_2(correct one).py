from tkinter import *
from PIL import ImageTk,Image
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
root=Tk()

def slide(n):
    global paused
    pygame.mixer.music.unpause()
    paused=False
    global song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0,start=slider.get())

    
def songtime():
  try:
    global song
    song2=MP3(song)
    global length
    length=song2.info.length
    songlength=time.strftime('%M:%S',time.gmtime(length))
    if int(slider.get()) == int(length):
        a_time.config(text=f'{songlength}/{songlength}')
        nex=music_list.get(0,"end").index(song.replace("D:/python/music/",""))
        n=nex+1
        song=music_list.get(n)
        song="D:/python/music/"+song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        music_list.selection_clear(0,END)
        music_list.activate(n)
        music_list.selection_set(n)
        slider.config(value=0)
    elif paused:
        pass
    else:
        slider_pos=int(length)
        slider.config(to=slider_pos,value=int(slider.get()))
        b_time=time.strftime('%M:%S',time.gmtime(int(slider.get())))
        a_time.config(text=f'{b_time}/{songlength}')
        next_time=int(slider.get())+1
        slider.config(value=next_time)
  except:
    pass
  a_time.after(1000,songtime)


def delete():
    global song
    if song==("D:/python/music/"+music_list.get(ACTIVE)):
        a_time.config(text='')
        slider.config(value=0)
        music_list.delete(ACTIVE)
        pygame.mixer.music.stop()
        song=""
    else:
        music_list.delete(ACTIVE)

def forward():
  try:
    global song
    nex=music_list.get(0,"end").index(song.replace("D:/python/music/",""))
    n=nex+1
    if (n+1)==music_list.index("end"):
        forward_button.config(state=DISABLED)
    if (n+1)>music_list.index("end"):
        return
    back_button.config(state=ACTIVE)
    global paused
    paused=False
    a_time.config(text='')
    slider.config(value=0)
    song=music_list.get(n)
    song="D:/python/music/"+song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    music_list.selection_clear(0,END)
    music_list.activate(n)
    music_list.selection_set(n,last=None)
  except:
    pass
def previous():
  try:
    global song
    nex=music_list.get(0,"end").index(song.replace("D:/python/music/",""))
    n=nex-1
    if n==0:
        back_button.config(state=DISABLED)
    if n<0:
        return
    forward_button.config(state=ACTIVE)
    global paused
    paused=False
    a_time.config(text='')
    slider.config(value=0)
    song=music_list.get(n)
    song="D:/python/music/"+song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    music_list.selection_clear(0,END)
    music_list.activate(n)
    music_list.selection_set(n,last=None)
  except:
    pass

def play():
  try:
    next=music_list.curselection()
    n=next[0]
    if (n+1)==music_list.index("end"):
        forward_button.config(state=DISABLED)
    else:
        forward_button.config(state=ACTIVE)
    if n==0:
        back_button.config(state=DISABLED)
    else:
        back_button.config(state=ACTIVE)
    global paused   
    paused=False
    slider.config(value=0)
    global stopped
    stopped=False
    global song
    song=music_list.get(ACTIVE)
    song="D:/python/music/"+song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
  except:
    pass

def add():
    songs=filedialog.askopenfilenames(initialdir="music/",title="choose a song",filetypes=(("mp3 files","*.mp3"),))
    for song in songs:
        x=song.replace("D:/python/music/","")
        music_list.insert(END,x)

def stop():
    root.quit()

paused=False
def pause(ispaused):
    global paused
    paused=ispaused
    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

song=""        
music_list=Listbox(root,bg="black",fg="white",width=60,selectbackground="gray")
music_list.pack(padx=20,pady=20)

pygame.mixer.init()

back_img=PhotoImage(file="python/back.png")
forward_img=PhotoImage(file="python/forward.png")
stop_img=PhotoImage(file="python/stop.png")
pause_img=PhotoImage(file="python/pause.png")
play_img=PhotoImage(file="python/play.png")

frame1=Frame(root)
frame1.pack()

back_button=Button(frame1,image=back_img,borderwidth=0,command=previous)
forward_button=Button(frame1,image=forward_img,borderwidth=0,command=forward)
stop_button=Button(frame1,image=stop_img,borderwidth=0,command=stop)
pause_button=Button(frame1,image=pause_img,borderwidth=0,command=lambda:pause(paused))
play_button=Button(frame1,image=play_img,borderwidth=0,command=play)

back_button.grid(row=0,column=0,padx=5)
forward_button.grid(row=0,column=4,padx=5)
stop_button.grid(row=0,column=2,padx=5)
pause_button.grid(row=0,column=1,padx=5)
play_button.grid(row=0,column=3,padx=5)

song_menu=Menu(root)
root.config(menu=song_menu)

add_menu=Menu(song_menu)
song_menu.add_cascade(label="Menu",menu=add_menu)
add_menu.add_command(label="Add Song",command=add)


remove=Menu(song_menu)
song_menu.add_cascade(label="delete",menu=remove)
remove.add_cascade(label="delete song",command=delete)

a_time=Label(root,text='',borderwidth=2,anchor=E)
a_time.pack(fill=X)

slider=ttk.Scale(root,from_=0,to=100,orient=HORIZONTAL,value=0,command=slide,length=400)
slider.pack()
songtime()


root.mainloop()