import requests
import json
# import datetime
import time
from selenium import webdriver
# import os
# from pprint import pprint

def YT_search(string):
    try:
        url = 'https://www.youtube.com/results?search_query={}'.format(string)
        
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        
        browser.get(url)
        # time.sleep(1)
        xpath = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a')
        href = xpath.get_attribute('href')
        browser.close()
        
        return href.split('=')[1]
    except:
        print('YT_search fail {}'.format(string))
        YT_search(string)

def KKboxCrawler(SongType, Area, Lang, Rank, Cate, Date):
    url = 'https://kma.kkbox.com/charts/api/v1/daily?category={}&date={}&lang={}&limit={}&terr={}&type={}'.format(Cate,Date,Lang,Rank,Area,SongType)
    res = requests.get(url)
    Orig_data = json.loads(res.text)
    Orig_data = Orig_data['data']['charts'][SongType]
    # print(Orig_data)
    ReturnData=[]
    for i in range(int(Rank)):
        rerurn_data={}
        #排名
        rerurn_data['RK'] = Orig_data[i]['rankings']['this_period']
        #歌名 不取'-'後面的內容
        rerurn_data['SongName'] = Orig_data[i]['song_name'].split(' -')[0].split(' (')[0].replace('?','')
        #歌手
        rerurn_data['Artist'] = Orig_data[i]['artist_name']
        #專輯
        rerurn_data['Album'] = Orig_data[i]['album_name']
        #縮圖 'https://i.kfs.io/album/' + 保留的地方 + '/fit/160x160.jpg'
        rerurn_data['ImgURL'] = Orig_data[i]['cover_image']['small'].split('album/')[1].split('/fit/')[0]
        #歌曲ID
        rerurn_data['SongID'] = Orig_data[i]['song_id'] 
        #上架日期         
        release_date = time.localtime(int(Orig_data[i]['release_date']))
        rerurn_data['ReleaseDate'] = time.strftime("%Y-%m-%d", release_date)
        
        ReturnData.append(rerurn_data)
        # ReturnData({'RK':*,'SongName':*,'Artist':*,'Album':*,'ImgURL':*,'SongID':*,'ReleaseDate':*})
    return ReturnData
    
def CateType(Lang,Area):
    url = 'https://kma.kkbox.com/charts/api/v1/daily/categories?lang={}&terr={}&type=song'.format(Lang,Area)
    res = requests.get(url)
    data = json.loads(res.text)
    cate = [data['data'][i]['category_name'] for i in range(len(data['data']))]
    # print('cate:',cate)
    return cate


#設定日期
# Yday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
# print(Yday)
# DBY = (datetime.date.today() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')
# print(DBY)



#參數說明
# =============================================================================
# KKboxCrawler(SongType, Area, Lang, Rank, Cate, Date)
# SongType類型參數: 單曲song, 新歌newrelease
# Area地區參數：台灣tw、香港hk、日本jp、新加坡sg、馬來西亞my -->預設tw
# Lang語言參數: 本地tc、簡中sc、日文ja、英文en、馬來ms --> 預設tc
# Rank名次參數: 取前幾名 1~50
# Cate曲風參數: 華語297,西洋390,日語308,韓語314,台語304,粵語320,綜合104,馬來917,西方771,亞洲861
# Date日期參數: --> 昨天Yday、前天DBY、自訂YYYY-MM-DD
# =============================================================================

# print(KKboxCrawler('song','tw','tc','1','297',Yday))


#爬音樂曲風 CateType(Lang,Area)
# print(CateType('tc','tw'))




