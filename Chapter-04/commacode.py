

def comma(a):
 n=len(a)
 l=[]
 if n==0:
  return a[0]
 else:
  l=','.join(a[:n-1])+',and,'+a[n-1]
  return 
     
a=list(map(str, input().split()))
print(comma(a))

