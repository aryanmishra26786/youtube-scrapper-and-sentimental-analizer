#Importing modules

from operator import index
from pickle import FALSE, TRUE
from turtle import right
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from pytube import YouTube
from youtube_comment_scraper_python import *
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from textblob import TextBlob


#data of you tube


option = Options()
option.headless = False

driver = webdriver.Firefox(options=option)
driver.implicitly_wait(5)
baseUrl = "https://www.youtube.com/"
keyword = "Iphone"


def getVideos():
    driver.get(f"{baseUrl}/search?q={keyword}")
    time.sleep(4)
    all_videos_tag=driver.find_elements(By.TAG_NAME,"ytd-video-renderer");
    videos_link=[]
    for parent in all_videos_tag:
        videos_link.append(
            parent.find_element(By.TAG_NAME,"a").get_attribute("href")
        )
    return videos_link
cvideo= getVideos()
def getChannelUrl():
    driver.get(f"{baseUrl}/search?q={keyword}")
    time.sleep(3)
    allChannelList=driver.find_elements(By.CSS_SELECTOR,"#text.style-scope.ytd-channel-name a.yt-simple-endpoint.style-scope.yt-formatted-string")
    links=list(dict.fromkeys(map(lambda a: a.get_attribute("href"),allChannelList)))
    return links 

def getChannelDetails(urls):
    global cvideo
    details= []
    count = 0
    for url in urls:
        driver.get(f"{url}/about")
        video_name=cvideo[count]
        cname = driver.find_element(By.CSS_SELECTOR,"#text.style-scope.ytd-channel-name").text
        cdess = driver.find_element(By.CSS_SELECTOR,"#description-container > yt-formatted-string:nth-child(2)").text
        subscriber= driver.find_element(By.CSS_SELECTOR,"#subscriber-count.style-scope.ytd-c4-tabbed-header-renderer").text
        clinks =url
        otherLinksobject=driver.find_elements(By.CSS_SELECTOR,"#link-list-container.style-scope.ytd-channel-about-metadata-renderer a.yt-simple-endpoint.style-scope.ytd-channel-about-metadata-renderer")
        otherLinks =list(dict.fromkeys(map(lambda a: a.get_attribute("href"),otherLinksobject)))
        object ={
            "keyword":keyword,
            "cname": cname,
            "subscriber": subscriber,
            "cdesc": cdess,
            "cvideo": video_name,
            "curl" : clinks,
            "otherLinks": otherLinks
            
        }
        count+=1
        details.append(object)
    return details
if __name__ == "__main__":
    # videos_link=getVideos()
    # print(videos_link)
    allChannelUrls = getChannelUrl()
    allChannelDetails = getChannelDetails(allChannelUrls) 
    A=allChannelDetails
    B= 'E:\python code\DATA_YOUTUBE.csv'
    
df = pd.DataFrame(A)
df.to_csv(B,index=False)
# videos_frame.




#comment scapping
 


df=pd.read_csv("E:\python code\DATA_YOUTUBE.csv")
links=df["cvideo"]
final_df = pd.DataFrame()
for i in  links:
    list1 = []
    link=i
    saved = 'E:\python code\Scrapped_comments.csv'
    youtube.open(link)
    response = youtube.video_comments()
    data = response['body']
    df = pd.DataFrame(data)
    for i in range(0,df.shape[0]):
        list1.append(link)
    df['Link'] = list1
    
    final_df = pd.concat([final_df,df],axis=0)
final_df.to_csv(saved)



aa = pd.read_csv("E:\python code\output.csv")  
aa.insert(0, column = "keyword", value = "keyword")  

  
df = pd.DataFrame(aa)
df.to_csv("E:\python code\output.csv",index=False)

    
    
    
    
#video download


df=pd.read_csv("E:\python code\DATA_YOUTUBE.csv")
links=df["cvideo"]
for i in  links:
    url=i
    my_video = YouTube(url)
    print("*********************Video Title************************")
    print(my_video.title)
    print("********************Tumbnail Image***********************")
    print(my_video.thumbnail_url)
    print("********************Download video*************************")
    for stream in my_video.streams:
        print(stream)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download("E:\python code")



#polarity of videos





polarity=[]
final_review=[]

cols = [1]
df = pd.read_csv("E:\python code\Scrapped_comments.csv", usecols=cols)
df = pd.DataFrame(df) 
li = df.values.tolist()
li
list1 = []
for i in li:
    list1.append(i[0])
comments=list1


for z in comments:

    b=[]
    # #finding polarity
    # blob1= TextBlob(paragraph)
    # print(blob1.sentiment)
    # p=blob1.sentiment
    # q=p[0]
    # polarity.append(q)       
    
    
      
    sentences = nltk.sent_tokenize(z)
    lemmatizer = WordNetLemmatizer()
    
    # Lemmatization
    for i in range(len(sentences)):
        words = nltk.word_tokenize(sentences[i])
        words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
        sentences[i] = ' '.join(words)
        a= sentences[i]
        b.append(a)
        k=b
    
            
    s= " "
    s=s.join(k)
    blob1= TextBlob(s)
    print(blob1.sentiment)
    p=blob1.sentiment
    q=p[0]
    polarity.append(q)

    
df=pd.DataFrame([polarity]).transpose()
df.to_csv("E:\python code\polization.csv")





#adding comments and polarity together





data1 = pd.read_csv('E:\python code\Scrapped_comments.csv')
data2 = pd.read_csv('E:\python code\polization.csv')
df = pd.concat([data1,data2], axis=1, ignore_index=False)
df.to_csv("C:\Users\yukta\OneDrive\Desktop\Youtube Scraping Project\output.csv")






