import pandas as pd  
numbers1=list(map(int,input("Enter the series1:").split()))
numbers2=list(map(int,input("Enter the series2:").split()))
op=input("enter the Operator:")
series1=pd.Series(numbers1)
series2=pd.Series(numbers2)
print(series1)
print(series2)
if(op=="+"):
    print(series1+series2)
elif(op=="-"):
    print(series1-series2)
elif(op=="*"):
    print(series1*series2)
elif(op=="/"):
    print(series1/series2)
elif(op=="%"):
    print(series1%series2)
else:
    print("enter the valid operator")
