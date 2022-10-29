# must of code are from stackoverflow.com
#!pip install requests
#!pip install BeautifulSoup
import requests
from bs4 import BeautifulSoup
import os
myfile="out.txt"
if os.path.isfile(myfile):
    os.remove(myfile)
else:
     pass


#it should be excactly number page of thread
n_pages = 19
# everything till 34680 need changed for diffrent thread
url = 'https://www.url.com/showthread.php?tid=4444&page='





for i in range (1,n_pages+1):
    link = url+str(i)
    r = requests.get(link, headers={'Cookie': 'PHPSESSID=notimportant'})
    soup = BeautifulSoup(r.content, 'html.parser')
    u_tag = soup.find_all('span', 'largetext')

    for user in u_tag:
        users=[]
        users.append(user.text)
        listToStr = ' '.join(map(str, users)) 
        list = listToStr
        list = list.replace('username', '')
        f = open('out.txt','a')
        print (list, file=f)
lines_seen = set()
with open("out.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
                     if i not in lines_seen:

                        lines_seen.add(i)

                        print(i.strip())
