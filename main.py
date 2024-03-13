from pygame import mixer
from tkinter import *
from PIL import ImageTk
import os

os.chdir(r'musicas')
musicas = os.listdir()



win = Tk()

win.geometry("700x500")

playImage = ImageTk.PhotoImage(file='../imagens/botao-play.png')
pauseImage = ImageTk.PhotoImage(file='../imagens/botao-pause.png')
unpauseImage = ImageTk.PhotoImage(file='../imagens/botao-unpause.png')
backImage = ImageTk.PhotoImage(file='../imagens/seta-para-a-esquerda.png')
nextImage = ImageTk.PhotoImage(file='../imagens/seta-para-a-direita.png')
img = ImageTk.PhotoImage(file='../imagens/YT_Music.jpg')
    
selected_index = 0

class App(Tk):    
    def __init__(self):
        self.win = win
        self.tela()
        self.buttons()
        self.frames_da_tela()
        self.listas()
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
        
        self.current_track = Label(self.frame_1, text='Current Track', bg='black', fg='white', width=48, height=1)
        self.current_track.pack()

        self.scrollbar = Scrollbar(self.frame_1, orient=VERTICAL)
        self.scrollbar.pack(side=LEFT, fill=Y)
        
    def listas(self):
        self.listbox = Listbox(self.frame_1, bg='#31363F', fg='white')
        self.listbox.pack()
        self.listbox.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
        for music in musicas:
            self.listbox.insert(END, music)    
            
    def buttons(self):
        self.bt_play = Button(self.win, bg='#31363F', image=playImage, text='>', command=lambda: play(self), relief='raised', overrelief='ridge')
        self.bt_play.pack()
        self.bt_play.place(relx=0.35, rely=0.88, relheight=0.08, relwidth=0.08)
        
        self.bt_pause = Button(self.win, bg='#31363F', image=pauseImage, text='| |', command=pause, relief='raised', overrelief='ridge')
        self.bt_pause.pack()
        self.bt_pause.place(relx=0.45, rely=0.88, relheight=0.08, relwidth=0.08)
        
        self.bt_unpause = Button(self.win, bg='#31363F',  image=unpauseImage, text='| >', command=unpause, relief='raised', overrelief='ridge')
        self.bt_unpause.pack()
        self.bt_unpause.place(relx=0.55, rely=0.88, relheight=0.08, relwidth=0.08)
        
        self.bt_next = Button(self.win, bg='#31363F', image=nextImage, text='>>', command=next_song, relief='raised', overrelief='ridge')
        self.bt_next.pack()
        self.bt_next.place(relx=0.65, rely=0.89, relheight=0.06, relwidth=0.06)
        
        self.bt_back = Button(self.win, bg='#31363F', image=backImage, text='<<', command=prev_song, relief='raised', overrelief='ridge')
        self.bt_back.pack()
        self.bt_back.place(relx=0.27, rely=0.89, relheight=0.06, relwidth=0.06)        
        
# def define_background():
#     bg = contents[current_song]['background'] 
#     print(bg)       
        
def play(self):
    global selected_index
    selected_index = self.listbox.curselection()[0]
    mixer.init()
    song = musicas[selected_index]
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
    global selected_index
    if(selected_index + 1 < len(musicas)):
        selected_index += 1
    else:
        selected_index = 0
    song = f'{musicas[selected_index]}'
    print(song, selected_index)
    mixer.music.load(song)
    mixer.music.play()
    
def prev_song():
    mixer.music.stop()
    global selected_index
    if(selected_index - 1 < 0):
        selected_index = len(musicas) - 1
    else:
        selected_index -= 1
    song = f'{musicas[selected_index]}'
    print(song, selected_index)
    mixer.music.load(song)
    mixer.music.play()


app_instance = App()
