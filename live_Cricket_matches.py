import requests, os, time
from bs4 import BeautifulSoup
r=requests.get("http://m.cricbuzz.com")
cric=BeautifulSoup(r.content)
m_list=[]


for matches in cric.find_all("span"):
    if(matches.get('class')==["matchheader"]):
        m_list.append(matches.text)

#MATCH LIST

m_list=list(set(m_list))
print "%d live matches found, Choose Yours:"%(len(m_list))
for i in m_list:
    print "%d. %s"%(m_list.index(i)+1,i)
ch_index=int(raw_input())-1
count=73
while(1==1):
    r=requests.get("http://m.cricbuzz.com")
    cric=BeautifulSoup(r.content)
    os.system('clear')
    for match in cric.find_all("span"):
        if(match.get('class')==["matchheader"] and match.text==m_list[ch_index]):
            stat=match.parent.parent.text
            cmd="notify-send -t 000 '%s'"%(stat)
            if(count>=75):
                count=0
                os.system(cmd)
            else:
                count=count+1
            print stat
            print count
            break
    time.sleep(2)