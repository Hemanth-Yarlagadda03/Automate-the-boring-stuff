import random

c=0
s=0
for i in range(10000):
 for i in range(100):
  a.append(random.randint(0,1))
  
 for i in range(len(a)):
  if a[i]==a[i-1]:
   c+=1
  if c==6:
   s+=1
 a=[]
print('percentage of streaks:',float(s/100),'%')
  

