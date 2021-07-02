i=int(input("Enter Number"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("sum of digits=",sum)   
 