num=[]
while True:
    n = int(input('n:'))
    if n==-9999:
        break
    num.append(n)
maxNum=0
for i in range(len(num)):
    for j in range(i,len(num)+1):
        if sum(num[i:j])>maxNum:
            maxNum=sum(num[i:j])
print(maxNum)