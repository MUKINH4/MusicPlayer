from pygame import mixer
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import json

json_data = './musicas/musicas.json'
with open(json_data, 'r') as j:
    contents = json.loads(j.read())



win = Tk()

win.geometry("700x500")

playImage = ImageTk.PhotoImage(file='imagens/botao-play.png')
pauseImage = ImageTk.PhotoImage(file='imagens/botao-pause.png')
unpauseImage = ImageTk.PhotoImage(file='imagens/botao-unpause.png')
backImage = ImageTk.PhotoImage(file='imagens/seta-para-a-esquerda.png')
nextImage = ImageTk.PhotoImage(file='imagens/seta-para-a-direita.png')
img = ImageTk.PhotoImage(file='imagens/YT_Music.jpg')
    
selected_index = 0
for index, music in enumerate(contents):
    if music['song']:
        selected_index = index
        print(selected_index)                      

class App(Tk):    
    def __init__(self):
        self.win = win
        self.tela()
        self.buttons()
        self.frames_da_tela()
        win.mainloop()
    def tela(self):
        self.win.title('Music Player') 
        self.win.resizable(False, False)
        self.win.configure(background='#76ABAE')
        self.win.geometry('800x600')
    def frames_da_tela(self):
        self.frame_1 = Frame(self.win, width=350, height=480)
        self.frame_1.configure(background='#31363F')
        self.frame_1.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        
        self.frame_2 = Frame(self.win, width=410, height=480)  
        self.frame_2.configure(background='#31363F')
        self.frame_2.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
        self.logo = Label(self.frame_2, image=img)
        self.logo.pack()
        #self.frame_1.place(relx=0.02, rely=0.02, relheight=0.8, relwidth=0.96)
        
    def buttons(self):
        self.bt_play = Button(self.win, bg='#31363F', image=playImage, text='>', command=play)
        self.bt_play.pack()
        self.bt_play.place(relx=0.35, rely=0.88, relheight=0.08, relwidth=0.08)
        
        self.bt_pause = Button(self.win, bg='#31363F', image=pauseImage, text='| |', command=pause)
        self.bt_pause.pack()
        self.bt_pause.place(relx=0.45, rely=0.88, relheight=0.08, relwidth=0.08)
        
        self.bt_unpause = Button(self.win, bg='#31363F',  image=unpauseImage, text='| >', command=unpause)
        self.bt_unpause.pack()
        self.bt_unpause.place(relx=0.55, rely=0.88, relheight=0.08, relwidth=0.08)
        
        self.bt_next = Button(self.win, bg='#31363F', image=nextImage, text='>>', command=next_song)
        self.bt_next.pack()
        self.bt_next.place(relx=0.65, rely=0.89, relheight=0.06, relwidth=0.06)
        
        self.bt_back = Button(self.win, bg='#31363F', image=backImage, text='<<', command=back_song)
        self.bt_back.pack()
        self.bt_back.place(relx=0.27, rely=0.89, relheight=0.06, relwidth=0.06)        
        
# def define_background():
#     bg = contents[current_song]['background'] 
#     print(bg)       
        
def play():
    mixer.init()
    song = f'musicas/{contents[selected_index]['song']}.mp3'
    mixer.music.load(song)
    mixer.music.play()
    if mixer.music.get_busy() == 0:
        next_song()
 
def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def next_song():
    mixer.music.stop()
    song = f'musicas/{contents[selected_index]['song']}.mp3'
    print(selected_index)
    mixer.music.load(song)
    mixer.music.play()
    
def back_song():
    mixer.music.stop()
    song = f'musicas/{contents[selected_index]['song']}.mp3'
    mixer.music.load(song)
    mixer.music.play()

App()
