import numpy as np

whole_data=np.load('whole_data.npy',allow_pickle=True)

np.random.shuffle(whole_data)


goodcount=0
badcount=0

gooddata=[] #在区间外的数据
baddata=[]  #在区间内的数据

for i in range(0,200000):
    if -0.2<(whole_data[i][1][1])<0.3:#不满足要求的
        badcount+=1
        baddata.append(whole_data[i])
    else:
        goodcount+=1
        gooddata.append(whole_data[i])
print(goodcount)
print(badcount)
print(goodcount+badcount)

for i in range(0,badcount):
    gooddata.append(baddata[i])

