#1
for i in range (151):
    print(i)

#2
for i in range (0,1001,1):
    if i % 5 == 0:
        print(i)

#3
for i in range (1,101,1):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else:
        print(i)

#4
sum = 0
for i in range (500001):
    if i%2!=0:
        sum=sum+i
print(sum)

#5
for i in range (2018,0,-4):
    print(i)

#6
lowNum=0
highNum=10
mult=2
for i in range (lowNum,highNum+1,1):
    if i%mult==0:
        print(i)
