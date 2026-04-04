import pandas as pd
import numpy as np

# s=pd.Series([10,20,30])
# s=pd.Series([10,20,30],index=["a","b","c"])
# s = pd.Series({'a': 1, 'b': 2, 'c': 3})
# print(s["a"])

# df=pd.DataFrame({
#     "Name":["alice","adi","dani"],
#     "Age":[23,45,32],
#     "City":["Delhi","Mumbai","Kolkata"]
# })
# df=pd.DataFrame([
#     {"name":"Alice","age": 34},
#     {"name":"Adi","age":34}
# ])
#  print(df)
# df=pd.DataFrame([[1,2,10],
#                [3,4],
#                [5,6],
#                [7,8]],columns=["A","B","C"])
# print (df)

dict1={
     "name":["harry","rohan","skillf","shubh"],
     "marks":[92,12,33,53],
     "city":["rampur","kolkata","bareilly","antarctica"]
}
df=pd.DataFrame(dict1)

df.to_csv("practical.csv",index=False)
# # print(df.describe())

# adi=pd.read_csv("practical.csv")
# # df.to_csv("output.csv", index=False)
# # print(df.head(4))

# newdf=df.to_excel("practical.xlsx", sheet_name="Sheet1")
# print(df[["name","marks"]])
# print(df.loc[1:2,[ "name","marks"]])
# print(df.iloc[0])
# print(df.iloc[0,1])
# print(df.iloc[:1,0:1])
# print(df[df["marks"]>25])

# df["salary"]=[2000,3847,5454,5655]
# df["marks"]=df["marks"]+1
# df["marks"]=df["marks"]+5
# df["marks"]=df["marks"].apply(lambda x: x+1)
# print(df)

# df.rename(columns={"name": "employees", "marks" : "bodycount"}, inplace=True)
# df["bodycount"]=df["bodycount"].astype(float)
# print(df )

# df.drop("city",axis=1,inplace=True)
# print (df)

# df.drop([0,1],axis=0 ,inplace=True)
# print(df)

# df.drop_duplicates(inplace =True)
# print (df)

# print( df.notnull())
# print(df.fillna(0))
# sorting=df.sort_index(ascending=False)
# print(sorting)

# group=df.groupby("city")["marks"].mean()
group= df.groupby(["city","name"])["marks"].sum()
print(group)