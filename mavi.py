# for i in range(1,101):
#    print(i)

n=10
sum=0
for i in range (1,n+1):
   sum+=i
   print(i)

print(sum)

print((n*(n+1))/2)

# num=1
# while num<=50:
#    if num%2==0:
#       print(num)
# num+=1

num1=54327
rev_num=0

while num1>0:
   rem= num1%10
   rev_num=rev_num*10+rem
   num1=num1//10


   rev_num=0
