import requests, pyautogui, base64, io, time

url = "http://127.0.0.1:23655"
pyautogui.screenshot('screenshot.png')

with open("screenshot.png", "rb") as image:
    b64string = base64.b64encode(image.read())
send = "i:" + str(b64string)[2:-1] + "~"

t0 = time.time()
for i in range(18):
	r = requests.post(url, headers = {'Content-Length' : str(len(send))},data =  {send.encode()})
t1 = time.time()
print(t1-t0)