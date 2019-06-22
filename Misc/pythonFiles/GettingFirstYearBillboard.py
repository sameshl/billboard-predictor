import pandas as pd
data=pd.read_csv('newBillSplit.csv',sep='\t')
dataset=data
#dataset.drop(dataset.columns[0],axis=1,inplace=True)
#dataset.drop('Track',axis=1,inplace=True)
#dataset.drop(dataset.columns[2:],axis=1,inplace=True)


v=dataset.artist_name.value_counts()
df=dataset[dataset.artist_name.isin(v.index[v.gt(1)])]
a=df.sort_values('year', ascending=True).drop_duplicates('artist_name').sort_index()

a.drop(a.columns[3:15],axis=1,inplace=True)

a.reset_index(drop=True,inplace=True)
a.to_csv('firstYearNewBill.csv',index=False,sep='\t')
