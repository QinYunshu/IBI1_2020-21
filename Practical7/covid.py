import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C://Users//Lenovo//IBI1_2020-21//Practical7")
covid_data=pd.read_csv("full_data.csv")
#show all columns, and every second row between (and including) 0 and 10
print(covid_data.iloc[0:11:2,:])
#use a Boolean to show “total cases” for all rows corresponding to Afghanistan.
data=[]
for i in range(0,7996):
    if covid_data.iloc[i,1]=="Afghanistan":
          data.append(True)
    else:
          data.append(False)
print(covid_data.loc[data,"total_cases"])

#compute the mean and median of new cases for the entire world.
#create a Boolean to show the data of "world"
world=[]
for i in range(0,7996):
    if covid_data.iloc[i,1]=="World":
          world.append(True)
    else:
          world.append(False)
world_new_cases=covid_data.iloc[world,2]
print(world_new_cases.mean())
print(world_new_cases.median())
#create a boxplot of new cases worldwide.
#plot both new cases and new deaths worldwide.
plt.boxplot(world_new_cases)
plt.ylabel("number")
plt.xlabel("new cases worldwide")
plt.title("the diatribution of new cases of Covid-19 worldwide")
plt.show()
world_new_deaths=covid_data.loc[world,"new_deaths"]
world_dates=covid_data.iloc[world,0]
plt.plot(world_dates,world_new_cases,'b+',world_dates,world_new_deaths,'c+')
plt.ylabel("number")
plt.xlabel("date")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
#code to answer the question stated in file question.txt
#the propotion of died cases in Germany
Germany_cases=covid_data.loc[covid_data.loc[:,"location"]=="Germany","total_cases"]
Germany_deaths=covid_data.loc[covid_data.loc[:,"location"]=="Germany","total_deaths"]
print(Germany_deaths.sum()/Germany_cases.sum())
#the propotion of died cases in UK
UK_cases=covid_data.loc[covid_data.loc[:,"location"]=="United Kingdom","total_cases"]
UK_deaths=covid_data.loc[covid_data.loc[:,"location"]=="United Kingdom","total_deaths"]
print(UK_deaths.sum()/UK_cases.sum())
