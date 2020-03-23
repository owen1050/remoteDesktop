import requests, pyautogui, base64, io

url = "http://127.0.0.1:23655"
pyautogui.screenshot('screenshot.png')

with open("screenshot.png", "rb") as image:
    b64string = base64.b64encode(image.read())

r = requests.post(url, data =  {"i:fdasfas".encode()})
