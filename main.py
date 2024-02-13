import pyautogui as pg
from time import sleep
from datetime import datetime, timedelta, time
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
with open(r"codes.txt", encoding="UTF-8") as c, open(r"lessons.txt", encoding="UTF-8") as l:
	c = {i.split(" - ")[0]: [i.split(" - ")[1], i.split(" - ")[2]] for i in c.read().split("\n")}
	l = {i.split("\n")[0]: i.split("\n")[1:]for i in l.read().split("\n\n")}
def f(i_c, c):
	pg.hotkey("winleft")
	sleep(10)
	pg.click(570, 619)
	sleep(20)
	pg.click(930, 542)
	sleep(20)
	pg.typewrite(i_c)
	pg.typewrite(["enter"])
	sleep(30)
	pg.typewrite(c)
	pg.typewrite(["enter"])
def hi():
	sleep(2*60)
	data, fs = sf.read(r'audio/1.wav')
	sd.play(data, fs)
	sd.wait()
# """
dt = datetime.today()
if dt.strftime("%A") in ("суббота", "воскресенье"):
	print("выходной")
else:
	print("не выходной!")
	if timedelta(hours=dt.hour, minutes=dt.minute) < timedelta(hours=8, minutes=30):
		x = timedelta(hours=8, minutes=30, seconds = 0) - timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
		print(f"sleep {x.seconds} seconds")
		sleep(x.seconds)
	t = time(datetime.today().hour, datetime.today().minute)
	y = l[dt.strftime("%A")]
	if t == time(8, 30):
		for i in y:
			f(c[i][0], c[i][1])
			# hi()
			sleep(45*60)
	else:
		while True:
			t = time(datetime.today().hour, datetime.today().minute)
			if dt.strftime("%A") != "пятница":
				if t == time(9, 20):
					f(c[y[1]][0], c[y[1]][1])
					# hi()
				elif t == time(10, 15):
					f(c[y[2]][0], c[y[2]][1])
					# hi()
				elif t == time(11, 10):
					f(c[y[3]][0], c[y[3]][1])
					# hi()
				elif t == time(12, 5):
					f(c[y[4]][0], c[y[4]][1])
					# hi()
				elif t == time(13, 0):
					f(c[y[5]][0], c[y[5]][1])
					# hi()
				elif t == time(13, 55):
					f(c[y[6]][0], c[y[6]][1])
					# hi()
					print(f"{datetime.today().strftime('%H:%M')} - Уроки закончились😀")
					break
			elif dt.strftime("%A") == "пятница":
				if t == time(9, 20):
					f(c[y[1]][0], c[y[1]][1])
					# hi()
				elif t == time(10, 15):
					f(c[y[2]][0], c[y[2]][1])
					# hi()
				elif t == time(11, 10):
					f(c[y[3]][0], c[y[3]][1])
					# hi()
				elif t == time(12, 5):
					f(c[y[4]][0], c[y[4]][1])
					# hi()
				elif t == time(13, 0):
					f(c[y[5]][0], c[y[5]][1])
					# hi()
					print(f"{datetime.today().strftime('%H:%M')} - Уроки закончились😀")
					break
			print(t)
			sleep(60)
# """