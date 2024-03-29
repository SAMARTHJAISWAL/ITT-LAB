
m = input("Please enter the start of the range: ")
n = input("Please enter the end of the range: ")

# Convert inputs to integers
m = int(m)
n = int(n)

for num in range (m,n+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
