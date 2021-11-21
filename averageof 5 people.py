i=1
sum=0
while i<=11:
    n=float(input("enter no"))
    sum=sum+n
    avg_weight=sum/11
    i=i+1
if avg_weight%5==0:
   print("divisible by 5")
else:
    print("not divisible by 5")
