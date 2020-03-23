import requests, pyautogui, base64, io, time

url = "http://127.0.0.1:23655"

t0 = time.time()
for i in range(18):
	r = requests.get(url, data =  {"i:~".encode()})
t1 = time.time()
print(t1-t0)

f = open("output.png", "wb")
f.write(io.BytesIO(base64.b64decode(r.text)).read())
f.close()