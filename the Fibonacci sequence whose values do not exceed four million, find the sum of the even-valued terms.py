odd,even=0,1
pavani=0
while True:
    odd,even=even,odd+even
    
    if even>=4000000:
        break
    if even%2==0:
        pavani+=even
print(pavani)
