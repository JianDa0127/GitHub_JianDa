from tkinter import *
import tkinter.ttk as ttk
from KKboxCrawler import KKboxCrawler,YT_search
from PIL import ImageTk
import requests
import os
from urllib.request import urlretrieve
from selenium import webdriver
import time
import yt_download
import vlc 
from pygame import mixer

# import testing

#建立kkbox_menu功能
def About():
    print('About')
def Setting():
    print('Setting')
def Close():
    print('Close')
#建立file_menu功能
def OpenFile():
    print('open file')
def OpenDir():
    print('open dir')
def OpenRecent():
    print('open recent')
#建立edit_menu功能
def CreateNewPlaylist():
    print('CreateNewPlaylist')
#建立control_menu功能
def Play():
    print('Play')
def Pause():
    print('Pause')
def Next():
    print('Next')
def Previous():
    print('Previous')
def VolumeUp():
    print('Volume Up')
def VolumeDown():
    print('Volume Down')
def Shuffle():
    print('Shuffle')
def Repeat():
    print('Repeat')
#建立account_menu功能
def HelloWorld():
    print('Hello World')
#建立help_menu功能
def Support():
    print('Support')

#建立選單項目
def menu_bar():
    #建立選單項目kkbox
    kkbox_menu = Menu(menubar,tearoff=False) 
    menubar.add_cascade(label='kkbox',menu=kkbox_menu)
    kkbox_menu.add_command(label='About',command=About)
    kkbox_menu.add_separator()
    kkbox_menu.add_command(label='Setting',command=Setting)
    kkbox_menu.add_separator()
    kkbox_menu.add_command(label='Close',command=Close)
    #建立選單項目file
    file_menu = Menu(menubar,tearoff=False) 
    menubar.add_cascade(label='File',menu=file_menu)
    file_menu.add_command(label='Open File',command=OpenFile)
    file_menu.add_command(label='Open Dir',command=OpenDir)
    file_menu.add_command(label='Open Recent',command=OpenRecent)
    #建立選單項目Edit
    edit_menu = Menu(menubar,tearoff=False) 
    menubar.add_cascade(label='Edit',menu=edit_menu)
    edit_menu.add_command(label='create new playlist',command=CreateNewPlaylist)
    #建立選單項目Control
    control_menu = Menu(menubar,tearoff=False) 
    menubar.add_cascade(label='File',menu=control_menu)
    control_menu.add_command(label='Play',command=Play)
    control_menu.add_command(label='Pause',command=Pause)
    control_menu.add_command(label='Next',command=Next)
    control_menu.add_command(label='Previous',command=Previous)
    control_menu.add_separator()
    control_menu.add_command(label='Volume Up',command=VolumeUp)
    control_menu.add_command(label='Volume Down',command=VolumeDown)
    control_menu.add_separator()
    control_menu.add_command(label='Shuffle',command=Shuffle)
    control_menu.add_command(label='Repeat',command=Repeat)
    #建立選單項目Account
    account_menu = Menu(menubar,tearoff=False) 
    menubar.add_cascade(label='Account',menu=account_menu)
    account_menu.add_command(label='Hello World',command=HelloWorld)
    #建立選單項目Help
    help_menu = Menu(menubar,tearoff=False) 
    menubar.add_cascade(label='Help',menu=help_menu)
    help_menu.add_command(label='Support',command=Support)

#取得歌詞
def get_lyrics():
    global col_id
    global PrintLyrics
    PrintLyrics.delete(0,END) #清空歌詞欄
    #讀取歌詞
    try:
        with open('./lyrics/{}.txt'.format(col_id),'r',encoding="utf-8") as f:
            lyrics = f.read()
    except:
        global SearchData_value
        SongType, Area, Lang = SearchData_value[0],SearchData_value[1],SearchData_value[2]
        Cate, Date = SearchData_value[4],SearchData_value[5]
        #背景執行
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        url = 'https://kma.kkbox.com/charts/daily/{}?cate={}&date={}&lang={}&terr={}'.format(SongType,Cate,Date,Lang,Area)
        browser.get(url)
        time.sleep(3)
        Rank = int(col_rank)+2 if int(col_rank)>30 else int(col_rank)+1
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[{}]/a/div/div[1]/span[1]/span[1]".format(Rank)).click()
        browser.implicitly_wait(5)
        #歌詞
        lyrics = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/p').text
        #儲存
        os.makedirs('./lyrics/',exist_ok=True)
        with open('./lyrics/{}.txt'.format(col_id),'w',encoding="utf-8") as f:
            f.write(lyrics)
        browser.close()
    #顯示歌詞
    lyrics = list(lyrics.replace('    ','\n').split('\n'))
    for i in lyrics:
        PrintLyrics.insert(END,i)

def Listen():
    global SearchData_value
    global col_rank
    global playMusic
    global playsong
    playsong = SearchData_value[1]+SearchData_value[4]+SearchData_value[0]+col_rank+SearchData_value[5]
    if os.path.isfile('{}.mp3'.format(playsong)):
        playmp3()
    else:
        global col_name
        global col_artist
        ytID = YT_search(col_artist + col_name)
        yt_download.Download(playsong,ytID)
        playmp3()
    #-----------------------------
def playmp3(): #播放
    global playsong,preplaysong
    global col_name
    if playsong==preplaysong: #同一首歌曲
        if not mixer.music.get_busy():
            mixer.music.load('{}.mp3'.format(playsong))
            mixer.music.play(loops=-1) 
        else:
            mixer.music.unpause() 
        var_play_title.set("正在播放：{}".format(col_name))
    else: # 更換歌曲
        playNewmp3()
        preplaysong=playsong 
        
def playNewmp3(): #播放新曲
    global playsong
    global col_name
    mixer.music.stop()
    mixer.music.load('{}.mp3'.format(playsong))   
    mixer.music.play(loops=-1)  
    var_play_title.set("正在播放：{}".format(col_name))
        #-----------------------------
def ListenPause():
    global col_name
    mixer.music.pause() 
    var_play_title.set("正在暫停播放：{}".format(col_name))
def ListenStop():
    mixer.music.stop()

def VolDown():
    global volume
    volume -=0.1
    if volume<=0.3:
        volume=0.3
    mixer.music.set_volume(volume)  
    
def VolUp():
    global volume
    volume +=0.1
    if volume>=1:
        volume=1
    mixer.music.set_volume(volume) 

def Stop():
    try:
        ListenStop()
    finally:
        root.destroy()

playsong=preplaysong = ""
volume=0.6

#查詢data按鈕
def SearchData():
    for i in tree.get_children(): tree.delete(i)
    SongType={'單曲':'song','新歌':'newrelease'}
    Area={'台灣':'tw','香港':'hk','日本':'jp','新加坡':'sg','馬來西亞':'my'}
    Lang={'本地':'tc','簡中':'sc','日文':'ja','英文':'en','馬來':'ms'}
    Cate={'華語':'297','西洋':'390','日語':'308','韓語':'314','台語':'304',
          '粵語':'320','綜合':'104','馬來':'917','西方':'771','亞洲':'861'}
    # Date={'昨天':'Yday','前天','DBY','自訂':'YYYY-MM-DD'}
    curr = SongType[var_curr.get()]
    area = Area[var_area.get()]
    lang = Lang[var_lang.get()]
    rank = var_rank.get()
    cate = Cate[var_cate.get()]
    date = var_date.get()
    #設定給其他函數使用的
    global SearchData_value
    SearchData_value=[curr,area,lang,rank,cate,date]
    #data查詢
    tree_title.set('{}{}前{}名 in {} {}'.format(var_cate.get(),var_curr.get(),rank,var_area.get(),date))
    data = KKboxCrawler(curr,area,lang,rank,cate,date)
    #顯示data
    for i in data:
        data_values=('{:02d}'.format(int(i['RK'])),i['SongName'],i['Artist'],i['Album'],i['ReleaseDate'],i['SongID'],i['ImgURL'])
        tree.insert('',index=END,text=i['RK'],values=data_values)

#清空data
def cleanData():
    for i in tree.get_children(): 
        tree.delete(i)

#下載圖片
def DownloadIMG(SongID,imgURL):
    os.makedirs('./img/',exist_ok=True)
    r = requests.get('https://i.kfs.io/album/{}/fit/160x160.jpg'.format(imgURL))
    with open('./img/{}.jpg'.format(SongID),'wb') as f:
        f.write(r.content)

def IMGresize(w,h,nw,nh,img):
    f1 = float(nw)/w
    f2 = float(nh)/h
    factor=min([f1,f2])
    width=int(w*factor)
    height=int(h*factor)
    return img.resize((width,height),Image.ANTIALIAS)

#事件-挑選歌曲
def treeSelect(event):
    global replaceIMG
    global col_id
    global col_rank
    global col_name
    global col_artist
    widgetObj = event.widget
    itemselected = widgetObj.selection()[0]
    col_rank = widgetObj.item(itemselected,'values')[0]
    col_name = widgetObj.item(itemselected,'values')[1]
    col_artist = widgetObj.item(itemselected,'values')[2]
    col_album = widgetObj.item(itemselected,'values')[3]
    col_date = widgetObj.item(itemselected,'values')[4]
    col_id = widgetObj.item(itemselected,'values')[5]
    col_img = widgetObj.item(itemselected,'values')[6]
    #更新圖片
    try:
        replaceIMG = ImageTk.open(file='./img/{}.jpg'.format(col_id))
        PrintIMG.configure(image=replaceIMG)
        PrintIMG.update_idletasks()
    except:
        DownloadIMG(col_id,col_img)
        replaceIMG = ImageTk.PhotoImage(file='./img/{}.jpg'.format(col_id))
        PrintIMG.configure(image=replaceIMG)
        PrintIMG.update_idletasks()
    #更新歌名、歌手、日期
    var_PrintSongName.set(col_name)
    var_PrintSinger.set(col_artist)
    var_PrintDate.set(col_date)
    #更新歌詞
    get_lyrics()

#基本配置
root = Tk()
root.title('TK_GUI')
root.configure(bg='#F0F8FF')
root.geometry('1000x600+100+30')
root.iconbitmap('icon/kkbox_favicon.ico')

#選單顯示
menubar = Menu(root,bd=30)  #建立主bar
menu_bar()                  #設定主bar
root.config(menu=menubar)   #顯示主bar

#歌詞顯示
Label_PrintLyrics = Label(root)
Label_PrintLyrics.place(x=670,y=25,width=300,height=390)
PrintLyrics = Listbox(Label_PrintLyrics)
# 歌詞顯示 的 ybar設定
lyrics_ybar = Scrollbar(Label_PrintLyrics)
lyrics_ybar.pack(side=RIGHT,fill=Y)
lyrics_ybar.config(command=PrintLyrics.yview)
PrintLyrics.configure(yscrollcommand=lyrics_ybar.set)
# 歌詞顯示 的 xbar設定
lyrics_xbar = Scrollbar(Label_PrintLyrics,orient=HORIZONTAL)
lyrics_xbar.pack(side=BOTTOM,fill=X)
lyrics_xbar.config(command=PrintLyrics.xview)
PrintLyrics.configure(xscrollcommand=lyrics_xbar.set)
PrintLyrics.pack(fill=BOTH,expand=True)
#圖片顯示設定
var_PrintIMG = PhotoImage(file = 'img/kkbox_app_icon.png')
PrintIMG = Label(root,image=var_PrintIMG)
PrintIMG.place(x=500,y=25,width=160,height=160)
#歌名顯示設定
var_PrintSongName = StringVar()
PrintSongName = Message(root,textvariable=var_PrintSongName,font='Helvtica 15 bold',relief=RIDGE,width=140)
PrintSongName.place(x=500,y=195,width=160,height=80)
var_PrintSongName.set('歌名')
#歌手顯示設定
var_PrintSinger = StringVar()
PrintSinger = Message(root,textvariable=var_PrintSinger,font='Helvtica 12',relief=RIDGE,width=140)
PrintSinger.place(x=500,y=285,width=160,height=80)
var_PrintSinger.set('歌手')
#日期顯示設定
var_PrintDate = StringVar()
PrintDate = Message(root,textvariable=var_PrintDate,font='Helvtica 12',relief=RIDGE,width=160)
PrintDate.place(x=500,y=375,width=160,height=40)
var_PrintDate.set('日期')


#播放事件
var_play_title = StringVar()
play_title = Label(root,textvariable=var_play_title,width=30,font='Helvtica 12')
var_play_title.set('----------')
play_title.place(x=520,y=430,width=440,height=45)
#播放開始
playImg=PhotoImage(file='img/play.png')
btnListen = Button(root,image=playImg,command=Listen,relief=RIDGE,width=10,height=1)
btnListen.place(x=520,y=490,width=60,height=60)
#播放暫停
pauseImg=PhotoImage(file='img/pause.png')
btnListenPause = Button(root,image=pauseImg,command=ListenPause,relief=RIDGE,width=10,height=1)
btnListenPause.place(x=615,y=490,width=60,height=60)
#播放停止
stopImg=PhotoImage(file='img/stop.png')
btnListenStop = Button(root,image=stopImg,command=ListenStop,relief=RIDGE,width=10,height=1)
btnListenStop.place(x=710,y=490,width=60,height=60)
#音量降低
voldownImg=PhotoImage(file='img/vol-down.png')
btnVolDown = Button(root,image=voldownImg,command=VolDown,relief=RIDGE,width=10,height=1)
btnVolDown.place(x=805,y=490,width=60,height=60)
#音量放大
volupImg=PhotoImage(file='img/vol-up.png')
btnVolUp = Button(root,image=volupImg,command=VolUp,relief=RIDGE,width=10,height=1)
btnVolUp.place(x=900,y=490,width=60,height=60)

#查詢data的選單設定
# =============================================================================
#curr_SongType_title設定
curr_SongType_title = Label(root,text='類別 Type',relief=RIDGE,width=12)
curr_SongType_title.place(x=41,y=25)
#area_SongType_title設定
area_SongType_title = Label(root,text='地區 Area',relief=RIDGE,width=12)
area_SongType_title.place(x=156,y=25)
#lang_SongType_title設定
lang_SongType_title = Label(root,text='語言 Lang',relief=RIDGE,width=12)
lang_SongType_title.place(x=271,y=25)
#rank_SongType_title設定
rank_SongType_title = Label(root,text='排名 Rank',relief=RIDGE,width=12)
rank_SongType_title.place(x=41,y=85)
#cate_SongType_title設定
cate_SongType_title = Label(root,text='曲風 Cate',relief=RIDGE,width=12)
cate_SongType_title.place(x=156,y=85)
#date_SongType_title設定
date_SongType_title = Label(root,text='日期 Date',relief=RIDGE,width=12)
date_SongType_title.place(x=271,y=85)
# =============================================================================
#var_curr設定
var_curr=StringVar()
curr_SongType = ttk.Combobox(root,textvariable=var_curr,width=10)
curr_SongType['value'] = ('單曲','新歌')
curr_SongType.current(0)
curr_SongType.place(x=40,y=50)
#var_area設定
var_area=StringVar()
area_SongType = ttk.Combobox(root,textvariable=var_area,width=10)
area_SongType['value'] = ('台灣','香港','日本','新加坡','馬來西亞')
area_SongType.current(0)
area_SongType.place(x=155,y=50)
#var_lang設定
var_lang=StringVar()
lang_SongType = ttk.Combobox(root,textvariable=var_lang,width=10)
lang_SongType['value'] = ('本地','簡中','日文','英文','馬來')
lang_SongType.current(0)
lang_SongType.place(x=270,y=50)
#var_rank設定
var_rank=StringVar()
rank_SongType = ttk.Combobox(root,textvariable=var_rank,width=10)
rank_SongType['value'] = [i for i in range(1,51)]
rank_SongType.current(49)
rank_SongType.place(x=40,y=110)
#var_cate設定
var_cate=StringVar()
cate_SongType = ttk.Combobox(root,textvariable=var_cate,width=10)
cate_SongType['value'] = ('華語','西洋','日語','韓語','台語','粵語','綜合','馬來','西方','亞洲')
cate_SongType.current(0)
cate_SongType.place(x=155,y=110)
#var_date設定
var_date=StringVar()
date_SongType = ttk.Combobox(root,textvariable=var_date,width=10)
date_SongType['value'] = ('2020-11-01','2020-11-15')
date_SongType.current(1)
date_SongType.place(x=270,y=110)
# =============================================================================
#查詢
btnSearch = Button(root,text='查詢',command=SearchData,relief=RIDGE,width=10,height=1)
btnSearch.place(x=385,y=40)
#清空
btnClean = Button(root,text='清空',command=cleanData,relief=RIDGE,width=10,height=1)
btnClean.place(x=385,y=90)


#查詢data 的 label設定
label_tree = Label(root)
label_tree.place(x=25,y=145,width=450,height=415)
#查詢data 的 標題設定
tree_title = StringVar()
label_tree_title = Label(label_tree,textvariable=tree_title,width=30)
tree_title.set('----------')
label_tree_title.pack()
#查詢表單 的 表單設定
tree = ttk.Treeview(label_tree,columns=('lab01','lab02','lab03','lab4','lab5','lab6','lab7'),show='headings')
tree_heading = ['RK','Rank','Song','Singer','Album','Date','SongID','img']
for i in range(8): #建立標頭
    tree.heading('#{}'.format(i), text=tree_heading[i])
tree.column('#1', width=40,anchor='center',minwidth=40)
tree.column('#2', width=140,anchor='center',minwidth=120)
tree.column('#3', width=170,anchor='center',minwidth=120)
tree.column('#4', width=150,anchor='center',minwidth=120)
tree.column('#5', width=120,anchor='center',minwidth=50)
tree.column('#6', width=150,anchor='center',minwidth=120)
tree.column('#7', width=120,anchor='center',minwidth=50)
#查詢data 的  表單ybar設定
tree_ybar = Scrollbar(label_tree)
tree_ybar.pack(side=RIGHT,fill=Y)
tree_ybar.config(command=tree.yview)
tree.configure(yscrollcommand=tree_ybar.set)
#查詢data 的  表單xbar設定
tree_xbar = Scrollbar(label_tree,orient=HORIZONTAL)
tree_xbar.pack(side=BOTTOM,fill=X)
tree_xbar.config(command=tree.xview)
tree.configure(xscrollcommand=tree_xbar.set)
#點選事件
tree.bind('<<TreeviewSelect>>',treeSelect)
#查詢data 的 定位
tree.pack(fill=BOTH,expand=True)

#顯示tk
root.protocol('WM_DELETE_WINDOW',Stop)
root.mainloop()