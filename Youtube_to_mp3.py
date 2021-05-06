import requests , json
from tqdm import tqdm
import requests, bs4, socket, os, time
from bs4 import BeautifulSoup as bSoup
from colorama import Fore, init
from tqdm import tqdm
init()
lg = Fore.LIGHTGREEN_EX
ly = Fore.LIGHTYELLOW_EX
lr = Fore.LIGHTRED_EX

banner = """
 █   █ ▀▀█▀▀ 　 ▀▀█▀▀ █▀▀█ 　 █▀▄▀█ █▀▀█ █▀▀█ 
 █▄▄▄█   █   　   █   █  █ 　 █ ▀ █ █  █   ▀▄ 
   █     █   　   ▀   ▀▀▀▀ 　 ▀   ▀ █▀▀▀ █▄▄█  
------------------------------------------------"""
tag = """   [+] Made By GH0STH4CK3R     [+] Version 2.0
------------------------------------------------"""

print(lg + banner)
print(ly + tag)
ytlink = input("Enter YT link : ")

try:
    ip = socket.gethostbyname("www.google.com")
except Exception as e:
    print(lr + "\nNo Internet !")
    time.sleep(5)
    exit()

# ---------------------------------------------------------------------------- HTTP REQUEST NO 1

url1 = "https://yt1s.com/api/ajaxSearch/index"

data = {"q": ytlink,"vt": "mp3"}

r = requests.post(url1,data=data)

response =  json.loads(r.text)

vid = response['vid']                # Get video id
k = response['kc']
title = response['title']            # Get title
a_rtist = response['a']
print(lg+"\nTitle    : ",title)
print("Uploader : ",a_rtist)

# ---------------------------------------------------------------------------- HTTP REQUEST NO 2

url2 = "https://yt1s.com/api/ajaxConvert/convert"

data = {"vid": vid,"k": k}

r2= requests.post(url2,data=data)
# ------------------------------------------------ Spinner
import sys
import time

print(ly+"")
def spinning_cursor():

    cs = ['Converting /','Converting -','Converting \\','Converting |']

    while True:
        for cursor in cs :
            yield cursor

spinner = spinning_cursor()
for _ in range(20):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b')    
#sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b') 

res = json.loads(r2.text)

dlink = res['dlink']              # Get download url
#print(res)


# ---------------------------------------------------------------------------- HTTP REQUEST NO 3

url3 = dlink

headers = {
    "authority": "dl228.iijjvii.biz",
    "method": "GET",
    "path": "/?file=M3R4SUNiN3JsOHJ6WWQ3aTdPRFA4NW1rRVJIOG10b0F0dndkN3lSb0lwMWdrc1prKytIckI5eEVLK3hFK1lPdkZKVmc1ei9PZE56QUhpeTYvYW9qVG5hQTVOTnp0QytjdFlncFZjeE9SaGZzazd2bXhCZHZoaExoYTlySVVPcHdZR2NvNWhKRmhXUEI2dWlHdEJUc3RqT3VxRURJSVc4SHV6OEZOUExZNWFCTHcyWGZVUHZoN0pRUXBpT2c5cE5FMzgrSnBnRGd4cjRCdHQ5bVlWWnhmNVZjeXAvSzg4YnByRlFidUw4KzIyenFwUEwxUUprd0UvaS9USEYxSmpJQSsrcjdWUllia25SSXFqenNyL2gzdnpKUFlyWW8rM1RsckE9PQ%3D%3D",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "referer": "https://yt1s.com/",
    "sec-ch-ua": "\"Chromium\";v=\"90\", \"Opera\";v=\"76\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 OPR/76.0.4017.94"
}

params = {"file": dlink}

r3 = requests.get(url3,stream=True)

tnm = str(title)
songname = tnm+".mp3"

rcode = r3.status_code              
print(lg+"")
if rcode == 200 :
    
    total = int(r3.headers.get('content-length', 0))   # Progressbar
    with open(songname, 'wb') as file, tqdm(
            desc=songname,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in r3.iter_content(chunk_size=1024):
            size = file.write(data)                     # Downloading
            bar.update(size)
    print("\nDownloaded > ",songname)        
    input("")
else :
    print("Download failed ! ",rcode)    
