import requests, pyautogui, base64, time
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk

data = ""
render = ""
img = ""
lastMouseSend = time.time()
class Window(Frame):
    def __init__(self, master=None):
        global data, render, img
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        

        im = Image.open(BytesIO(base64.b64decode(data)))
        
        render = ImageTk.PhotoImage(im)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

def updateImg():
    global data, render, root,img
    url = "http://127.0.0.1:23655"
    r = requests.get(url, data =  {"i:~".encode()})
    data = r.text
    im = Image.open(BytesIO(base64.b64decode(data)))        
    render = ImageTk.PhotoImage(im)
    img.config(image = render)
    root.after(500,updateImg)
    print("RAN")

def motion(event):
    global lastMouseSend
    if(time.time() - lastMouseSend > 0.5):

        url = "http://127.0.0.1:23655"
        send = "cp:" + str(event.x)+"," + str(event.y) + "~"
        r = requests.post(url, data =  {send.encode()})
        print(r.text)
        lastMouseSend = time.time()

url = "http://127.0.0.1:23655"
r = requests.get(url, data =  {"i:~".encode()})
data = r.text

root = Tk()

app = Window(root)
root.after(1000,updateImg)
root.bind('<Motion>', motion)
root.wm_title("Tkinter window")
root.geometry("200x120")
root.mainloop()

