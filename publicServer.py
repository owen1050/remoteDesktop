from http.server import BaseHTTPRequestHandler, HTTPServer
import time, threading, requests, os, pyautogui, base64, io

from pynput import keyboard

runServer = True
htpd = 1
image_str = ""
to_click = False
click_pos_x = 0
click_pos_y = 0
cursor_pos_x = 0
cursor_pos_y = 0
keys_to_press = ""

class httpServer(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        return

    def do_GET(self):
        global image_str, to_click, click_pos_x, click_pos_y, cursor_pos_x, cursor_pos_y, keys_to_press
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()

        ret = ""
        
        post_raw_str = ""
        post_raw = 0
        while(post_raw != "b\'~\'"):
            post_raw= str(self.rfile.read(1))
            post_raw_str = post_raw_str + post_raw[2]
            
        post_str = post_raw_str
        post_type = post_str[0:post_str.find(":")]
        post_data = post_str[post_str.find(":")+1:]

        if(post_type == "i"):
            print("sent image")
            ret = image_str

        if(post_type == "cp"):
            print("sent cursor position")
            ret = str(cursor_pos_x) + "," +str(cursor_pos_y) + "~"

        if(post_type == "cc"):
            if(to_click):
                to_click = False
                ret = str(click_pos_x) + "," + str(click_pos_y) +"~"
                print("sent click pos")

        if(post_type == "kb"):
            print("sent kb")
            ret = keys_to_press 
            keys_to_press = ""

        self.wfile.write(ret.encode())

    def do_POST(self):
        global image_str, to_click, click_pos_x, click_pos_y, cursor_pos_x, cursor_pos_y, keys_to_press
        ret = ""

        post_raw_str = ""
        post_raw = 0
        while(post_raw != "b\'~\'"):
            post_raw= str(self.rfile.read(1))
            post_raw_str = post_raw_str + post_raw[2]
            
        post_str = post_raw_str
        post_type = post_str[0:post_str.find(":")]
        post_data = post_str[post_str.find(":")+1:]

        if(post_type == "i"):
            print("new image")
            ret = "new image added"
            image_str = post_data


        if(post_type == "cp"):
            print("new cursor position")
            cursor_pos_x = int(post_data[0:post_data.find(",")])
            cursor_pos_y = int(post_data[post_data.find(",")+1:post_data.find("~")])
            ret = "New cursor pos set to " + str(cursor_pos_x) + ":" + str(cursor_pos_y)

        if(post_type == "cc"):
            print("new cursor click")
            to_click = True
            click_pos_x = int(post_data[0:post_data.find(",")])
            click_pos_y = int(post_data[post_data.find(",")+1:post_data.find("~")])
            print(click_pos_x)
            print(click_pos_y)
            ret = "New click pos set to " + str(click_pos_x) + ":" + str(click_pos_y)
        if(post_type == "kb"):
            print("new kb")
            keys_to_press = keys_to_press+   post_data[0:-1]+","
            ret = "added keys"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        if(ret == ""):
            ret = "no return string specfied"
        self.wfile.write(ret.encode())


def on_press(key):
    global httpd
    if(str(key) == "Key.up"):
        httpd.shutdown()
        print("server = false")


def run():
    global httpd
    httpd = HTTPServer(('', 23655), httpServer)
    print ("Starting http server on 23655")
    httpd.serve_forever()     
    print("Shutdown server") 


listener = keyboard.Listener(
    on_press=on_press)
listener.start()
run()