import math
import pandas as pd
#CSVの読み込み
data_path="perf.csv"
perf_data=pd.read_csv(data_path,header=0,index_col=0)
User_name=list(perf_data.columns)
open_count=len(perf_data[User_name[0]])+1

#今回の分の行を追加
perf_data.loc[open_count-1]=-1

#今回のコンテストでのパフォーマンスを入力&CSVに書き込み
for i in User_name:
    if i=="name":
        continue
    print(i)
    perf=int(input())
    perf_data[i][open_count-1]=perf

#各々のレーティングの計算
for i in User_name:
    if i=="name":
        continue
    rate=0
    #参加回数を数える
    part_count=open_count
    for j in range(open_count):
        if perf_data[i][j]==-1:
            part_count-=1
    part_count_ref=part_count
    #レート(第二段階)を計算
    for j in range(open_count):
        if perf_data[i][j]!=-1:
            rate+=2**(perf_data[i][j]/800)*(0.9**part_count_ref)
            part_count_ref-=1
    rate/=0.9*(1-0.9**part_count)/(1-0.9)
    rate=800*math.log2(rate)
    #リセマラ対策補正をかける
    rate-=(math.sqrt(1-0.81**part_count)/(1-0.9**part_count)-1)/(math.sqrt(19)-1)*1200

    #400以下なら補正する
    if rate<=400:
        rate=400/math.exp((400-rate)/400)
    #レーティングの出力
    print(i,int(rate+0.5))

#保存
perf_data.to_csv(data_path)
