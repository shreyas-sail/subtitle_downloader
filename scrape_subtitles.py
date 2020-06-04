num_movie=1
num_sub=1

from bs4 import BeautifulSoup as soup
import urllib2
import wget
import re
import requests


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
downloader='https://www.yifysubtitles.com/search?q=get%20out'
# downloader=base_url+sub_url
# downloader=str(downloader)

# print(downloader)

down_soup=get_url(downloader)

class_name=re.compile('^main')

down_lik = down_soup.findAll("div",{"class":"media-body"})
#zeroth_link=down_lik[0]
for names in down_lik:
    
    
    print(names.div.h3.text + "\t\t"+ "("+str(num_movie)+")" )
    print("\n")
    num_movie+=1
print(num_movie)

## slecting movie out of the list

print("\n\n\n\n")



valid=True

while valid:
    seleted_num=int(input("Select the number number "))
    if ((num_movie-1) >= seleted_num) :
        x=seleted_num-1
        selected_link=down_lik[x]
        print('\n')
        print(selected_link.a["href"])
        selected_movie_link=selected_link.a["href"]
        print("\n")
        valid=False
    else:
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

        valid1=False
    else:
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