from itertools import permutations
from random import choice

def Check_AB(X, Y):
    A = len([1 for i in range(len(Y)) if Y[i]==X[i]])
    B = len(set(Y)&set(X))-A
    return A,B

Data = list(permutations([ _ for _ in range(10)],4))
guessTimes=0
while True:
    comGuess = list(choice(Data))   #電腦猜的數
    guessTimes+=1
    print('第{}次猜題:{}'.format(guessTimes,comGuess))
    a, b =map(int,input('請輸入A、B值(空格分隔):').split())
    Data = [data for data in Data if (Check_AB(data,comGuess)==(a,b))]
    print(len(Data))
    if len(Data)==1:
        break
print('你的答案是:{}'.format(Data[0]))






