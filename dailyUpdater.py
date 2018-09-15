import tkinter as tk
from bs4 import BeautifulSoup
import requests

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

url = requests.get('https://www.google.com/search?client=ubuntu&channel=fs&q=temperature+near+me&ie=utf-8&oe=utf-8', headers=headers)
urlContent = BeautifulSoup(url.content, "lxml")

url2 = requests.get('https://www.exchangerates.org.uk/Dollars-to-Rupees-currency-conversion-page.html', headers=headers)
url2Content = BeautifulSoup(url.content, "lxml")


class Updater(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.find_stuff()

	def find_stuff(self):
		self.temp_btn = tk.Button(root, command = self.get_temp)
		self.temp_btn.pack()
		self.temp_label = tk.Label(root)
		self.temp_label.pack()

		self.rupe_btn = tk.Button(root, command = self.get_rupe)
		self.rupe_btn.pack()
		self.rupe_label = tk.Label(root)
		self.rupe_label.pack()

	def get_temp(self):
		temp = urlContent.find('span', {'id' : 'wob_tm'})
		temp = temp.text
		self.temp_label.configure(text= "Temp: " + str(temp))

	def get_rupe(self):
		rupe = url2Content.find('div', {'class' : 'p_conv30'})
		rupe = rupe.find('span', {'id' : 'shd2a'})
		rupe = rupe.find('span', {'id' : 'shd2b'})
		rupe = rupe.text
		self.rupe_label.configure(text= "Rupee: " + str(rupe))

root = tk.Tk()
root.title("Daily Updater")
root.geometry("265x180")
root.resizable(width=False, height=False)
app = Updater(master= root)
app.mainloop()