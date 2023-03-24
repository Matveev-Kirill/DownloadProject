import requests
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
import os

#Function to download videos 
def dowload():
    path = txt_path.get()
    link = txt_link.get()
    qual = combobox.get()
    if len(path) == 0 or len(link) == 0: 
        messagebox.showinfo('Error','Check link or path')
    else:
        try:
            yt = YouTube(link)
            my_video = yt.streams.filter(res=qual).first()
            my_video.download(path)
            messagebox.showinfo('Success','Download successful')
        except:
            messagebox.showinfo('Error','Change the quality or check if the link to the video is correct')

#Change the directory where the video will be uploaded
def browseFiles():
    filename = filedialog.askdirectory()
    txt_path.insert(0, filename)
    path = txt_path.get()
    if len(path) == 0:
        txt_path.insert(0, os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
#Clears the string with the old path       
def clear():
    txt_path.delete(0, END)
#Disables the ability to click on buttons if there is no way to access YouTube
def ButtonOff(button):
    button.configure(state = DISABLED)

window = Tk()
window.title("Downloader")
window.geometry('540x250')

lbl_link = Label(window, text="Link: ")
lbl_link.grid(column=0, row=1, pady=10, padx=10)

txt_link = Entry(window, width=50)
txt_link.grid(column=1, row=1)
Link = txt_link.get()

txt_path = Entry(window, width=50)
txt_path.grid(column=1, row=3)
txt_path.insert(0, os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))

btn = Button(window, text="Download", command=dowload)
btn.grid(column=1, row=2,pady=4, padx=10)

lbl_path = Label(window, text="Path: ")
lbl_path.grid(column=0, row=3, pady=10, padx=10)

btn_path = Button(window, text="Choose directory", command=lambda: [clear(),browseFiles()])
btn_path.grid(column=1, row=4)
#Running a test request to YouTube
connection_check = requests.get('https://www.youtube.com/')
status = str(connection_check.status_code)[0]
if (status == '1') | (status == '2'):
    lbl_status = Label(window, text="YouTube is online", fg= 'green')
else:
    lbl_status = Label(window, text="YouTube is ofline", fg= 'red')
    ButtonOff(btn)
    ButtonOff(btn_path)
lbl_status.grid(column=1, row=0, pady=10, padx=10)

quality = ('144p','240p','360p','480p','720p','1080p','1440p','2160p')
var = StringVar()
combobox = ttk.Combobox(window, textvariable = var)
combobox['values'] = quality
combobox['state'] = 'readonly'
combobox.grid(column=2, row=1, pady=10, padx=10)
combobox.current(0)


q_link = Label(window, text="Quality")
q_link.grid(column=2, row=0, pady=10, padx=10)
window.mainloop()

