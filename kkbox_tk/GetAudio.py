from urllib.request import urlretrieve
from selenium import webdriver
import time

def get_audio(SongType, Area, Lang, Rank, Cate, Date):
    #背景執行
    # options = webdriver.ChromeOptions() 
    # options.add_argument('--headless')    
    # driver = webdriver.Chrome(chrome_options=options, executable_path="./chromedriver.exe") # 背景執行
    
    url = 'https://kma.kkbox.com/charts/daily/{}?cate={}&date={}&lang={}&terr={}'.format(SongType,Cate,Date,Lang,Area)
    browser = webdriver.Chrome() 
    browser.get(url)
    time.sleep(3)

    Rank = int(Rank)+1 if int(Rank)>30 else int(Rank)
    for i in range(2,Rank+2):
        if i == 32: continue #跳過例外
        #單曲頁面
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[{}]/a/div/div[1]/span[1]/span[1]".format(i)).click()
        browser.implicitly_wait(5)
        #歌詞
        # lyrics = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/p').text
        # print(lyrics)
        #試聽檔案
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/button[1]").click()
        browser.implicitly_wait(5)
        audio = browser.find_element_by_tag_name('audio') #試聽檔案位置
        
        #儲存試聽檔案
        song_name = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/h1').text
        song_name = song_name.split(' -')[0].split(' (')[0].replace('?','')
        try:
            urlretrieve(audio.get_attribute('src'),"{}.mp3".format(i-2 if i>32 else i-1,song_name))
            print('[Success 30s download]',song_name)
        except:
            print('[Fail 30s download]',song_name)
            pass
        time.sleep(1)
        browser.back() #上一頁
    #關瀏覽器
    browser.close()
    
    #回傳歌詞(未實現的待改功能)
    # return lyrics

# 測試 get_audio(SongType, Area, Lang, Rank, Cate, Date)
get_audio('song','tw','tc','20','104','2020-11-15')
