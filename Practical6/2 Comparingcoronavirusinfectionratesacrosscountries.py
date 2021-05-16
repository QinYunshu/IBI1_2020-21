#make a dictionary 
frequency={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
sizes=[frequency['USA'],frequency['India'],frequency['Brazil'],frequency['Russia'],frequency['UK']]
#to set the figure of the pieplot 
explode=(0,0,0,0,0)
plt.title("The frequency table")
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
