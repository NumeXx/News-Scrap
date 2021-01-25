# News Scraping
# Author NumeX

import os
import time
import requests
import json
link='https://opennewsapi.herokuapp.com/api/news/'
os.system('cls || clear')
print("#--------------------------------------#")
print("[#] Tools By : NumeX")
print("[#] News Scraper Tools")
print("[#] Github : https://github.com/NumeXx")
print("#--------------------------------------#\n")
try:
    r = requests.get(link)
    n = json.loads(r .text)
except requests.ConnectionError:
    print('[x] Tolong Periksa Koneksi internet anda')
for data in n['results']:
    print(100*'=')
    print('sumber  :', data['source'])
    print('tag     :', data['tag'])
    print('tanggal :', data['created_at'])
    print('judul   :', data['title'])
    print('link    :', data['link'])
    print('gambar  :', data['image'])
    time.sleep(0.09)