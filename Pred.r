setwd("Desktop/")
df = read.csv('Mining.csv')
colnames(df)
Train = df[1:250, 1:7 ]
Test = df[250:312 , 1:7 ]
Train_data = Train[, 1:6]
Test_data = Test[, 1:6]
Train_res = Train[, 7:7]
Test_res = Test[, 7:7]

plot(Train_data$Brand, Train_res)
library(rpart)
First = rpart(Train_res ~ Brand + RAM + Display + Touch + OS, Train_data) 
p = predict(First, Test_data)
plot(Test_res, p)

Df1 = NULL
DF1$res = p
Df1$True = Test_res

