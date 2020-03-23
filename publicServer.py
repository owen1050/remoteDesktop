from http.server import BaseHTTPRequestHandler, HTTPServer
import time, threading, requests, os

class httpServer(BaseHTTPRequestHandler):
    image_str = ""
    to_click = False
    click_pos_x = 0
    click_pos_y = 0
    cursor_pos_x = 0
    cursor_pos_y = 0
    

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Get up test".encode())

    def do_POST(self):
        ret = ""

        if(self.headers['isNewImage'] == '1'):
            print("new image")

        content_len = int(self.headers.get('Content-Length'))
        post_raw= str(self.rfile.read(content_len))
        post_str = str(post_raw[3:-2])
        post_type = post_str[0:post_str.find(":")]
        post_data = post_str[post_str.find(":")+1:]
        #print(post_data)

        if(post_type == "i"):
            print("new image")
            ret = "new image added"
            image_str = post_data

        if(post_type == "cp"):
            print("new cursor position")
            cursor_pos_x = int(post_data[0:post_data.find(",")])
            cursor_pos_y = int(post_data[post_data.find(",")+1:])
            print(cursor_pos_x)
            print(cursor_pos_y)
            ret = "New cursor pos set to " + str(cursor_pos_x) + ":" + str(cursor_pos_y)

        if(post_type == "cc"):
            print("new cursor click")
            to_click = True
            click_pos_x = int(post_data[0:post_data.find(",")])
            click_pos_y = int(post_data[post_data.find(",")+1:])
            print(click_pos_x)
            print(click_pos_y)
            ret = "New click pos set to " + str(click_pos_x) + ":" + str(click_pos_y)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        if(ret == ""):
            ret = "no return string specfied"
        self.wfile.write(ret.encode())


def run():
    httpd = HTTPServer(('', 23655), httpServer)
    print ("Starting http server on 23655")
    try:         
        httpd.serve_forever()     
    except:         
        httpd.shutdown()         
        print("Shutdown server") 

run()