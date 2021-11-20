from math import log,factorial

vetorx=[0]*10

for i in range(0,10):
    if i%2==0:
        vetorx[i]= (3**i)+7*factorial(i)
        
    elif i%2!=0:
        vetorx[i]=(2**1) + (4*log(i))
print(vetorx)
    
soma=0
maior=0
p=0
posmaior=0
for elemento in vetorx:
    soma+=elemento
    p+=1
    if elemento>maior:
        maior=elemento
        posmaior=p
        
media=soma/10
print(media)    
print(maior)
print(posmaior)