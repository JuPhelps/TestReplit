import pandas as pd
import numpy as np
from func import func

print(func(100))

s = pd.Series([100,200,300,400])

print("hello world")

a = ["a","b","c","d","e"]

for i in range(0,len(a)):
  print(a[i])
  print(i)

for i in range(0,len(s)):
  print(i)
  print(s[i])

f = open("textfl.txt")
contents = f.read()
f.close()
print(contents)
print("make file")
f = open("newfile.txt", "w")
f.write("add this")
f.close()

df = pd.read_csv('csvtest.csv', header=None)
print(df)
print(df.loc[1][1])
print(df[1])
print(df.loc[:,1])
print(df.loc[2,:])
print(df.iloc[0,:])
print(df.iloc[:,0:1])
print("end")
