pavani=[123,456,789,963,852,741,159,951,753]
if pavani[0]>pavani[1]:
    num1,num2=pavani[0],pavani[1]
else:
    num1,num2=pavani[1],pavani[0]
for x in pavani[2:]:
    if x>num2:
        if x>num1:
            num2 ,num1=num1,x
        else:
            num2=x
print(num2)
