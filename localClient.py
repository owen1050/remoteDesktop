import requests, pyautogui, base64, io, time

url = "http://192.168.1.196:23655"
t0 = 0
while(True):
	if(True): #time.time() - t0 >1):
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


		r = requests.get(url,data =  {"cp:~".encode()})	
		try:
			x = int(r.text[0:r.text.find(",")])
			y = int(r.text[r.text.find(",")+1:r.text.find("~")])
			print(x,y,"MOVE")
			pyautogui.moveTo(x,y)
		except:
			pass

		r = requests.get(url,data =  {"cc:~".encode()})	
		try:
			x = int(r.text[0:r.text.find(",")])
			y = int(r.text[r.text.find(",")+1:r.text.find("~")])
			print(x,y, "CLICK")
			pyautogui.click(x = x,y = y)
		except:
			pass

		r = requests.get(url,data =  {"kb:~".encode()})
		data = r.text
		print(data)
		try:
			while(len(data) > 1):
				k = data[0:data.find(",")]
				if(k == "BackSpace"):
					pyautogui.press("backspace")
				else:
					pyautogui.press(k)
				print("pressed" + str(k))
				data = data[data.find(",")+1:]
		except:
			pass
