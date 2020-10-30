import random as ra
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#獲取猜測數的A,B值
def GetAB(set_num,guess_num):   
    a = len(['' for i in range(4) if set_num[i] == guess_num[i]])
    b = len(set(set_num)&set(guess_num)) - a 
    return str(a)+str(b)

#主迴圈
def Run(LoopTimes):     
    for i in range(LoopTimes):
        ans_data = Orig_data             #解答資料組合設定為:初始Data
        for ans in ans_data:
            times=0
            guess_data = Orig_data
            while 1:
                times+=1
                guess = guess_data[0]    #猜測資料: 資料過濾後的第一組開始猜
                ab = GetAB(ans, guess)
                
                #過濾資料
                if ab=='40':
                    CountTimesList[times-1]+=1
                    break
                else: 
                    guess_data = [num for num in guess_data if (GetAB(num,guess)==ab)]
                    if len(guess_data) == 1:
                        times+=1
                        CountTimesList[times-1]+=1
                        break

#初始化Data
Orig_data = list(__import__('itertools').permutations([i for i in range(10)], 4))

#測試迴圈數量
LoopTimes = 1
print('LoopTimes =',LoopTimes)

#獲取猜測次數表
CountTimesList=np.array([0 for i in range(10)])
Run(LoopTimes)

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
#df = pd.DataFrame({'counts':CountTimesList,'prob':GuessTimes_prob}, index=GuessTimesList)
#print(df.transpose())
print('index',GuessTimesList)
print('Counts',CountTimesList)
print('prob',GuessTimes_prob)

#計算總平均及標準差
StatMean =  sum(CountTimesList * GuessTimesList) / AllGuess
StatStd = (sum(GuessTimesList**2*CountTimesList)/sum(CountTimesList) - StatMean**2)**0.5
print('Mean=%.4f Std=%.4f'%(StatMean, StatStd))