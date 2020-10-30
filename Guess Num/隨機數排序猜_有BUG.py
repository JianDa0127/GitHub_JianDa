import random as ra
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def GetAB(set_num,guess_num):
    a = len([0 for i in range(4) if set_num[i] == guess_num[i]])
    b = len(set(set_num)&set(guess_num)) - a 
    return a,b
def ChoseData(ans,guess,data):
    a,b = GetAB(ans,guess)
    tran_data = [num for num in data if (GetAB(num,guess)==(a,b))]
    return tran_data
  
Orig_data = list(__import__('itertools').permutations([1,2,3,4,5,6,7,8,9,0], 4))

def run(run_times):
    run_times_list=[]
    for i in range(run_times):
        #ans = list(ra.choice(Orig_data))
        ans_data = Orig_data
        for ans in ans_data:
            times=0
            sample_data = Orig_data
            while 1:
                times+=1
                #guess = list(ra.choice(sample_data))
                guess = sample_data[0]
                sample_data = ChoseData(ans,guess,sample_data)
                if times==10:
                    run_times_list.append(10)
                    break
                else:
                    if len(sample_data)==1:
                        run_times_list.append(times)
                        break
    return run_times_list

#rt_list_num = int(input('run_times=')) 
rt_list_num = 1
rt_list = run(rt_list_num)


X_bar = np.array([x for x in range(1,11)])
Y = np.array([rt_list.count(i) for i in X_bar])
Y_bar = Y/rt_list_num

plt.bar(X_bar,Y_bar)
plt.title('PDF (n='+str(rt_list_num)+')')
plt.xlabel('Times')
plt.ylabel('probability')
plt.show()

df = pd.DataFrame(Y, columns=['counts'], index=X_bar)
print(df.transpose())

print('mean={} std={} range=({},{})'.format(np.mean(rt_list),np.std(rt_list),min(rt_list),max(rt_list)))