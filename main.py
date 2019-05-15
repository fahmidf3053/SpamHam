import pandas as pd
import numpy as np
import math

# data = pd.read_csv("spam.csv",header=None)
# # print(data)
#
# data1= data[data.iloc[:, 57]==0]
# data2= data[data.iloc[:, 57]==1]
#
# total=np.zeros((54,2),dtype=int)
# prob=np.zeros((54,2))
# for x in range (0,54):
#     total[x][0]=data1[x].sum()
#     total[x][1]=data2[x].sum()
#
#     prob[x][0]=total[x][0]/(total[x][0]+total[x][1])
#     prob[x][1]=1- prob[x][0]
#
#     print("Ham probabilty",x+1,"===",prob[x][0])
#     print("Spam probabilty",x+1,"===",prob[x][1])


def hst(train,test):
    data1= train[train.iloc[:, 57]==0]
    data2= train[train.iloc[:, 57]==1]

    total=np.zeros((54,2),dtype=int)
    prob=np.zeros((54,2))
    for x in range (0,54):
        total[x][0]=data1[x].sum()
        total[x][1]=data2[x].sum()

        prob[x][0]=total[x][0]/(total[x][0]+total[x][1])
        prob[x][1]=1- prob[x][0]


    ham=0
    spam=0

    for x in range (0, 54):
         if test[x] !=0 :

             if prob[x][0] > 0:
                 prob[x][0]=prob[x][0]
             else :
                 prob[x][0]=1

             if prob[x][1] > 0:
                 prob[x][1]=prob[x][1]
             else :
                 prob[x][1]=1






             # print(prob[x][0])
             # print(prob[x][1])

             ham=ham+math.log(prob[x][0])
             spam=spam+math.log(prob[x][1])

    cls=12

    if ham>spam :
        cls=0
    else :
        cls =1

    return cls



def main():
    data = pd.read_csv("spam.csv",header=None)

    index = len(data)

    par=int(.1*index)-1
    parcent=0
    #print(par)
    for x in range(10):

        testSegment = data.iloc[x*par:(x*par+(par-1))]

        trainSegement = data.drop(data.index[x*par:(x*par+(par-1))])
        #print(len(testSegment))

        match=0
        for y in range(len(testSegment)):
            cls=hst(trainSegement, testSegment.iloc[y])
            #print(cls)
            #print(testSegment.iloc[y][4])
            if cls==testSegment.iloc[y][57]:
                #print("ami asi ",y," number e")
                match+=1


            #print(testSegment.iloc[0])
        print(match)
        parcent+=match/(par*10)


    print("Result is: ",parcent*100,"%")



main()




# ham=1
# spam=1
#
# for x in range (0, 54):
#     if data1.iloc[1][x] !=0 :
#         ham=ham*prob[x][0]
#         spam=spam*prob[x][1]
#
#
# if ham > spam:
#     print("Ham")
#
# else :
#     print("spam")
