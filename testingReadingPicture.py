import pyautogui, base64, io

pyautogui.screenshot('screenshot.png')

with open("screenshot.png", "rb") as image:
    b64string = base64.b64encode(image.read())

f = open("output.png", "wb")
f.write(io.BytesIO(base64.b64decode(b64string)).read())
f.close()
