from gtts import gTTS
import speech_recognition as sr
import pyaudio
import os
import webbrowser as wb
from playsound import playsound
import smtplib
import random

##scarping
from bs4 import BeautifulSoup as soup
import urllib2
import wget
import re
import requests
############


r=sr.Recognizer()
r1=sr.Recognizer()
r3=sr.Recognizer()

def plays(path):
    playsound(path)


def talkToMe(audio):
    tts=gTTS(text=audio,lang='en',slow=False)
    r=random.randint(1,10000000)
    audio_filename="audi"+str(r)+'.mp3'
    tts.save(audio_filename)
    playsound(audio_filename)
    print(audio)
    os.remove(audio_filename)

  #starting command  
# def Mycommand():
#     r= sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening.......")
#         r.pause_threshold = 0.5
#         r.adjust_for_ambient_noise(source, duration =1)
#         audio=r.listen(source)
        
                

#         try:
#             command=r.recognize_google(audio)
#             print('You said  '+command+'\n')
#             return command
#         #loop back
#         except sr.UnknownValueError:
#             talkToMe("Sorry couldn't get that")
#             assistant(Mycommand())





def search_sub():
    r3=sr.Recognizer()
    talkToMe("Movie name please ")
    with sr.Microphone() as source:
        r3.pause_threshold=1
        r3.adjust_for_ambient_noise(source,duration=1)
        audio=r3.listen(source)

        try:
            movie_name=r3.recognize_google(audio)
            print(movie_name+"\n")
            return movie_name
        except sr.UnknownValueError:
            talkToMe("didn't get that")

            

 #searching command           
# def assistant(command):
#     if 'subtitle' in command:
#         movie=search_sub()
#         url='https://www.yifysubtitles.com/search?q='
#         movie=search_sub()
#         wb.get().open_new(url+movie)

# while True:
#     assistant(Mycommand())


movie=search_sub()
if movie==None:
    search_sub()
    
movie=str(movie)
url='https://www.yifysubtitles.com/search?q='

wb.get().open_new_tab(url+movie)
movie=url+movie

######################################-------------------------------------------------------------#####################################################
######################################-------------------------------------------------------------#####################################################
######################################-------------------------------------------------------------#####################################################
######################################-------------------------------------------------------------#####################################################
######################################-------------------------------------------------------------#####################################################
######################################-------------------------------------------------------------#####################################################


num_movie=1
num_sub=1




#just variables


base_url="https://www.yifysubtitles.com/"
main_url="https://www.yifysubtitles.com/search?q="

def get_url(my_url):
    req=urllib2.Request(my_url)

    uclient=urllib2.urlopen(req)#making connections

    page_html=uclient.read()#content of the page

    uclient.close()#closing

    page_so=soup(page_html,"html.parser")

    return page_so

page_soup=get_url(main_url)


# containers=page_soup.findAll('div',{'class':'media-body'})

# mo_link=page_soup.findAll("div",{"class":"media-left media-middle"})
# i=mo_link[0]
# print(i.a["href"])
# sub_url=i.a["href"]
downloader=movie
# downloader=base_url+sub_url
# downloader=str(downloader)

# print(downloader)

down_soup=get_url(downloader)

class_name=re.compile('^main')

down_lik = down_soup.findAll("div",{"class":"media-body"})
#zeroth_link=down_lik[0]
if len(down_soup)==0:
    talkToMe("no subtitle avaiable on yify")
    exit()


for names in down_lik:
    
    
    print(names.div.h3.text + "\t\t"+ "("+str(num_movie)+")" )
    print("\n")
    num_movie+=1
print(num_movie)

## slecting movie out of the list

print("\n\n\n\n")



valid=True

while valid:
    talkToMe("type in the movie number")
    seleted_num=int(input("Select the movie number "))
    
    if ((num_movie-1) >= seleted_num) :
        x=seleted_num-1
        selected_link=down_lik[x]
        print('\n')
        print(selected_link.a["href"])
        selected_movie_link=selected_link.a["href"]
        print("\n")
        valid=False
    else:
        talkToMe("Select proper number of the movie ")

        print("Select proper number of the movie ")
        
##end of selecting_link

##scrape inside selected link

inside_link=str(base_url)+str(selected_movie_link) 
inside_soup=get_url(inside_link)

en_link=inside_soup.findAll("td",{"class":"flag-cell"})

#getting only english subtitles

print('\n')

link_list=[]
for lang in en_link:
    if lang.span.next.text=='English':
        link_list.append(lang.nextSibling.a["href"])

for i in range(5):
    print(link_list[i]+'\t'+'('+str(num_sub)+')')
    num_sub+=1
    print('\n')

##selecting subs
valid1=True
while valid1:
    talkToMe("type in the subtitle number")
    seleted_sub_num=int(input("Select the sub number "))
    
    if ((num_sub-1) >= seleted_sub_num) :
        x=seleted_sub_num-1
        final_link=str(base_url)+str(link_list[seleted_sub_num])
        final_soup=get_url(final_link)

        final_download=final_soup.findAll("a",{"class":"btn-icon download-subtitle"})
        f=final_download[0]
        final_download_link=f["href"]
        print(final_download_link+'\n\n')
        mynewsub=wget.download(final_download_link)
        print('\n')
        talkToMe("the subtitle has been downloded check your desktop page")

        valid1=False
    else:
        talkToMe("select proper number")

        print("select proper number")
        









# in_url='https://www.opensubtitles.org/en/subtitles/8192263/birds-of-prey-and-the-fantabulous-emancipation-of-one-harley-quinn-en'
# in_soup=get_url(in_url)

# in_down=in_soup.findAll("form",{"name":"moviehash"})
# x=in_down[0]
# print("\n\n")
# print(x.a["href"])
# download_link=x.a["href"]
# y="https://www.yifysubtitles.com/subtitle/getout2017bluray720p-1080px264-sparks-english-108942.zip"

# filename=wget.download(y)

# r=requests.get(y)

# with open('sub1.srt','wb') as f:
#     f.write(r.content)



#filename_xx=wget.download(y)



# print(x["href"])
# sub_download_link=x["href"]

# download_link=base_url+sub_download_link
# print("\n\n")
# print(download_link)






# for container in containers:
#     mo_name=container.h3.text

    # imdb_rating=page_soup.findAll("span",{"class":"movinfo-section"})
    # print(imdb_rating.text)
    # print("\n")



