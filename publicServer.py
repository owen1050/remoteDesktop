from http.server import BaseHTTPRequestHandler, HTTPServer
import time, threading, requests, os

class httpServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write("your Request has been processed".encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("post".encode())


def run():
    httpd = HTTPServer(('', 23655), httpServer)
    print ("Starting http server on 23655")
    try:         
        httpd.serve_forever()     
    except:         
        httpd.shutdown()         
        print("Shutdown server") 

run()