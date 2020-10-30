import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#獲取猜測數的A,B值
def GetAB(set_num,guess_num):   
  a = len(['' for i in range(4) if set_num[i] == guess_num[i]])
  b = len(set(set_num)&set(guess_num)) - a 
  return a,b

#將Data過濾，過濾成相同A,B值的Data
def FilterData(guess, data):
  global ans
  a,b = GetAB(ans, guess)
  filter_datas = [num for num in data if (GetAB(num,guess)==(a,b))]
  return filter_datas

#窮舉法loop
def LoopRun(Guess_times,Datas,mLen):
    global flag
    Guess_times+=1
    for guess in Datas:   
        guess_data = FilterData(guess,Datas)
        
        #讓我知道程式還活著，可省略
        if Guess_times==1:                                  
            flag += 1 
            if flag!=1 and (flag-1)%56==0:
                print()
                print(CountTimesList)
                print('guess {}'.format(guess))
            print('.',end='')                               
        
        #避免例外狀況，目前未觸發過
        if Guess_times>10:
            CountTimesList[Guess_times-1]+=(1.0/mLen*5040)  #次數機率校正
            break
        
        #如果過濾資料後僅剩一組資料，將 校正後之次數機率 加入 猜測次數表
        if len(guess_data)==1:  
            CountTimesList[Guess_times-1]+=(1.0/mLen*5040)  #次數機率校正
        else:
            LoopRun(Guess_times,guess_data,len(guess_data)*mLen)

#初始化Data
Orig_data = list(__import__('itertools').permutations([i for i in range(10)], 4))

#測試迴圈數量
print('LoopTimes = 1')

#獲取猜測次數表
CountTimesList = np.array([0.0000 for i in range(11)])
flag = 0        #讓我知道程式還活著，可省略

#窮舉法
ans = Orig_data[0]
print('ans =',ans)
LoopRun(0,Orig_data,5040)   #loop

#預先設定後面程式常用之變數: 猜測次數表的index、總猜測次數
GuessTimesList = np.array([x for x in range(1,11)])
AllGuess = sum(CountTimesList)

#猜測次數機率表，取到小數第四位
GuessTimes_prob = np.around(CountTimesList/AllGuess,decimals=4)

#繪製長條圖
plt.bar(GuessTimesList,GuessTimes_prob)
plt.title('AllRunTimes='+str(AllGuess))
plt.xlabel('Times')
plt.ylabel('probability')
plt.show()

#建立表格並輸出
df = pd.DataFrame({'counts':CountTimesList,'prob':GuessTimes_prob}, index=GuessTimesList)
print(df.transpose())

#計算總平均及標準差
StatMean =  sum(CountTimesList * GuessTimesList) / AllGuess
StatStd = (sum(GuessTimesList**2*CountTimesList)/sum(CountTimesList) - StatMean**2)**0.5
print('Mean=%.4f Std=%.4f'%(StatMean, StatStd))