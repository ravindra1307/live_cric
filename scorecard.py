import requests, time, pynotify
from bs4 import BeautifulSoup

#GETTING LIVE MATCHES LIST

base_url="http://m.cricbuzz.com"
r=requests.get(base_url)
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

#Match_Choice

ch_index=int(raw_input())-1

#GETTING MATCH Link

for match in cric.find_all("span"):
        if(match.get('class')==["matchheader"] and match.text==m_list[ch_index]):
            match_link=match.parent.parent.parent.parent.get('href')
            break

#SHOWING SCORE

while(1==1):
#GETTING MATCH

    match_src=requests.get(base_url+match_link)
    match_scr=BeautifulSoup(match_src.content)

#TEAM SCORE AND STATUS

    stat=[]
    ctm=0
    for match in match_scr.find_all("span"):
        try:
            if(match.get('class')[0]=="cbz-ui-status" or match.get('class')[0]=="crr"):
                stat.append(match.text)
            if(match.get('class')[0]=="ui-allscores"):
                stat.append(match.text)
            if(match.get('class')==["bat-bowl-miniscore"] and ctm!=2):
                a=""
                ct=1
                for j in match.parent.parent.parent.parent.children:
                    a+=(j.text+" ")
                    if(ct==2):
                        stat.append(a)
                        break
                    ct+=1
                ctm+=1
        except:
            continue
    status=""
    for k in stat:
        status+=(k+'\n')

    pynotify.init("ak")
    n=pynotify.Notification(m_list[ch_index],status)
    n.set_timeout(25)
    n.show()
    time.sleep(200)