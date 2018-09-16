import tkinter as tk
from bs4 import BeautifulSoup
import requests

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

url = requests.get('https://www.google.com/search?client=ubuntu&channel=fs&q=temperature+near+me&ie=utf-8&oe=utf-8', headers=headers)
urlContent = BeautifulSoup(url.content, "lxml")

url2 = requests.get('https://www.google.com/search?client=ubuntu&hs=tNu&channel=fs&ei=-FWeW8iWEonUvgTyzpToBg&q=dollar+vs+rupee&oq=dollar&gs_l=psy-ab.1.0.0i67k1j0i131i67k1j0i7i30k1j0i131k1j0i131i67k1j0i7i30k1j0i131i67k1j0i67k1j0i7i30k1l2.32332.32332.0.34191.1.1.0.0.0.0.336.336.3-1.1.0....0...1.1.64.psy-ab..0.1.335....0.-qxo0Ixmfbk', headers=headers)
url2Content = BeautifulSoup(url2.content, "lxml")

url3 = requests.get('http://www.wordthink.com/', headers=headers)
url3Content = BeautifulSoup(url3.content, "lxml")


class Updater(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.find_stuff()

	def find_stuff(self):
		self.temp_btn = tk.Button(root, text="Today's Temperature", command = self.get_temp)
		self.temp_btn.pack()
		self.temp_label = tk.Label(root)
		self.temp_label.pack()

		self.rupe_btn = tk.Button(root, text="Dollar v/s Rupee", command = self.get_rupe)
		self.rupe_btn.pack()
		self.rupe_label = tk.Label(root)
		self.rupe_label.pack()

		self.word_btn = tk.Button(root, text="Today's Word", command = self.get_word)
		self.word_btn.pack()
		self.word_label = tk.Label(root, wraplength=250)
		self.word_label.pack()

	def get_temp(self):
		temp = urlContent.find('span', {'id' : 'wob_tm'})
		temp = temp.text
		self.temp_label.configure(text= "Temp: " + str(temp))

	def get_rupe(self):
		rupe = url2Content.find('span', {'id' : 'knowledge-currency__tgt-amount'})
		rupe = rupe.text
		self.rupe_label.configure(text= "Rupee: " + str(rupe))	

	def get_word(self):
		word = url3Content.find('div', {'id' : 'post-728'})
		word2 = word.find('p').text
		self.word_label.configure(text= "" + str(word2))

root = tk.Tk()
root.title("Daily Updater")
root.geometry("465x250")
root.resizable(width=False, height=False)
app = Updater(master=root)
app.mainloop()