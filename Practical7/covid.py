import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C://Users//Lenovo//IBI1_2020-21//Practical7")
covid_data=pd.read_csv("full_data.csv")
#show all columns, and every second row between (and including) 0 and 10
covid_data.iloc[0:11:2,:]
#use a Boolean to show “total cases” for all rows corresponding to Afghanistan.



#compute the mean and median of new cases for the entire world.
#create a boxplot of new cases worldwide.
#plot both new cases and new deaths worldwide.
#There is code to answer the question stated in file question.txt
#The code to answer the question runs without errors
#The code to answer the question does what it is meant to do
#All plots are clearly labell
