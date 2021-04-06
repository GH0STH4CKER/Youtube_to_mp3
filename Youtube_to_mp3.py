import requests , bs4 , socket , os , time
from bs4 import BeautifulSoup as bSoup
from colorama import Fore , init
init() 
lg = Fore.LIGHTGREEN_EX
ly = Fore.LIGHTYELLOW_EX
lr = Fore.LIGHTRED_EX

banner = """
 █   █ ▀▀█▀▀ 　 ▀▀█▀▀ █▀▀█ 　 █▀▄▀█ █▀▀█ █▀▀█ 
 █▄▄▄█   █   　   █   █  █ 　 █ ▀ █ █  █   ▀▄ 
   █     █   　   ▀   ▀▀▀▀ 　 ▀   ▀ █▀▀▀ █▄▄█  
------------------------------------------------"""
tag = """   [+] Made By GH0STH4CK3R     [+] Version 1.0
------------------------------------------------"""

print(lg + banner)
print(ly + tag)

try:
    ip = socket.gethostbyname("www.google.com")  
except Exception as e:
    print(lr+ "\nNo Internet !")  
    time.sleep(5)
    exit()    
print(lg +"")
ytlink = input("Enter YT Link : ")

if 'youtu.be' in ytlink :
	ysplit = ytlink.split('youtu.be/')
	yc = ysplit[1]
	ytlink = "https://www.youtube.com/watch?v="+yc
#print(ytlink)

#ytlink = "https://www."+ytlink
try:
    ytcode = ytlink.split('=')[1]
except Exception as ee:
    print("Invlid Url Type !")
    time.sleep(5)
    exit()

url = "https://www.320youtube.com/v25/convert"
params = {"v": ytlink}
#Sample https://www.youtube.com/watch?v=A57B7B6w3kw

res = requests.get(url,params=params)

url1 = "https://www.320youtube.com/v25/watch"
params1 = {"v": ytcode}

res1 = requests.get(url1,params=params1)

#print(res1.status_code)
data = res1.text

if "<form action" in data :
    
    page_soup = bSoup(data,"html.parser")

    html = page_soup.find_all("form")
    
    titles = page_soup.find_all("h4")
    details = page_soup.find_all("small")
     
    title = str(titles[0]).replace('<h4>','')
    title = title.replace('</h4>','')

    detail = str(details[0]).replace('<small>','')
    detail = detail.replace('</small>','')

    d_link = html[0]['action']

    print("\nTitle: ",title)
    print("")
    print(detail)

    print("\nDownload link : ",d_link) 

    res2 = requests.get(d_link)

    songname = title+".mp3"

    #print("Downloading...")
    file = open(songname, "wb")
    file.write(res2.content)
    file.close()

    print("\nFile Download Success !")

else : 
    print(lr + "SOmething went wrong !")

input("\n[ Thank you for using my program ~ GH0STH4CK3R ]") 

