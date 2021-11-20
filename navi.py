 
i=0
for numero in range(1,5000000):
    if numero%2==0 and numero%49==0 and numero%37==0:
        i+=1
print(i)
