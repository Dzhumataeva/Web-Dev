a=int(input())
i=0
sum=0
while(a>0):
    k=a%10
    sum+=k*2**i
    a//=10
    i+=1
print(sum)
