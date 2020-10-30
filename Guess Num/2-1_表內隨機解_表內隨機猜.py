from itertools import permutations
from random import choice
import matplotlib.pyplot as plt

def Check_AB(X, Y):
    A = len([1 for i in range(len(Y)) if Y[i]==X[i]])
    B = len(set(Y)&set(X))-A
    return str(A)+'A'+str(B)+'B'  

TimesList =[]
LoopTimes = int(input('模擬次數:'))
#print('模擬{}次'.format(LoopTimes))
Data = list(permutations([ _ for _ in range(10)],4)) #母體組合

for i in range(LoopTimes): 
    ans = list(choice(Data))
    guessTimes=0
    GuessData = Data
    while True:
        guess = list(choice(GuessData))   #電腦猜的數
        guessTimes+=1
        ab = Check_AB(ans,guess)  
        if ab=='4A0B':
            TimesList.append(guessTimes)
            break
        else:
            GuessData = [data for data in GuessData if (Check_AB(guess,data)==ab)]

xbar = [x for x in range(1,max(TimesList)+2)]
print('Guess Times',xbar)
ybar = [TimesList.count(i) for i in xbar]
print('Probability',ybar)

plt.bar(xbar,ybar)
plt.xlabel('guess times')
plt.ylabel('probability')
plt.show()