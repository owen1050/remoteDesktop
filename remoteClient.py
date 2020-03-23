import requests, pyautogui, base64, time
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk

data = ""
render = ""
img = ""
lastMouseSend = time.time()
lastClickSend = time.time()
mx = 0
my = 0
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
    global data, render, root,img,  mx,my
    url = "http://127.0.0.1:23655"
    r = requests.get(url, data =  {"i:~".encode()})
    data = r.text
    im = Image.open(BytesIO(base64.b64decode(data)))        
    render = ImageTk.PhotoImage(im)
    img.config(image = render)
    url = "http://127.0.0.1:23655"
    send = "cp:" + str(mx)+"," + str(my) + "~"
    r = requests.post(url, data =  {send.encode()})
    
    root.after(100,updateImg)
    print("RAN")

def motion(event):
    global lastMouseSend, mx,my
    mx = event.x
    my = event.y
    
def click(event):
    global lastClickSend
    if(time.time() - lastClickSend > 0.5):

        url = "http://127.0.0.1:23655"
        send = "cc:" + str(event.x)+"," + str(event.y) + "~"
        r = requests.post(url, data =  {send.encode()})
        print(r.text)
        lastClickSend = time.time()
def keyboard(event):
    url = "http://127.0.0.1:23655"
    send = "kb:" + str(event.keysym)+ "~"
    r = requests.post(url, data =  {send.encode()})
    print(event.keysym)


url = "http://127.0.0.1:23655"
r = requests.get(url, data =  {"i:~".encode()})
data = r.text

root = Tk()

app = Window(root)
root.after(1000,updateImg)
root.bind('<Motion>', motion)
root.bind("<Button-1>", click)
root.bind('<Key>', keyboard)
root.wm_title("Tkinter window")
root.geometry("1920x1080")
root.mainloop()

