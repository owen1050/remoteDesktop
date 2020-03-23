import requests, pyautogui, base64, io, time

url = "http://127.0.0.1:23655"
t0 = 0
while(True):
	if(time.time() - t0 >1):
		t01 = time.time()
		ss = pyautogui.screenshot()

		buffer = io.BytesIO()
		ss.save(buffer, format = "JPEG")
		ss = buffer.getvalue()
		b64string = base64.b64encode(ss)
		send = "i:" + str(b64string)[2:-1] + "~"
		r = requests.post(url,data =  {send.encode()})
		print(len(send))
		print(time.time() - t01)
		t0 = time.time()
