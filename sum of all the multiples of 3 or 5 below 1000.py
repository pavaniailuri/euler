max=1000
result=0
for i in range(0,max):
    if i%3==0 or i%5==0:
        print i
        result+=i
print result
