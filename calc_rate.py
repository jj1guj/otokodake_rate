from math import *
User={"jj1guj":0,"v1t4n":0,"tomatotatsuya":0}
Perfoemance={}
perf_sum=0
Part_count={}
N=int(input())
User_name=list(User.keys())
for i in User_name:
    print(i)
    perf,part=map(int,input().split())
    Part_count[i]=part
    Perfoemance[i]=perf

#レートを算出
for i in User_name:
    User[i]=800*log2(2**(Perfoemance[i]/800))
    User[i]-=(sqrt(1-0.81)/(1-0.9)-1)/(sqrt(19)-1)*1200
    if User[i]<=400:
        User[i]=400/e**((400-User[i])/400)
    print(i,int(User[i]+0.5))

#CSVへの書き込み
