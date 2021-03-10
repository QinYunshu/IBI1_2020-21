r=1.2
n=84
# use i to present the number of rounds
i=0
while i<5:
 n=n*(r+1)
 i=i+1
 if i==5:
  break
print "The r rate is",r,"meaning",r,"individuals will be infected by each indi$
print "After 5 generations the total number of individuals infected is",n
