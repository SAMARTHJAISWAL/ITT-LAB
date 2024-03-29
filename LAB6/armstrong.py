sum=0
num=int(input("enter"))
temp=num
while(temp>0):
    d=temp%10
    sum+=d**3
    temp//=10
if (num==sum):
    print("armstrong")
else:
    print("not")
