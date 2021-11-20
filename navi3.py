def peganota(n1,n2,n3,n4,n5,a1,a2,a3,a4,a5):
    dic={a1:n1, a2:n2, a3:n3, a4:n4, a5:n5}
    print('oi')
    max=0
    chave=''
    melhor=''
    for k,v in dic.items():

        if v>max:
            max=v
            chave=k
    melhor=chave
    print(melhor,max)
    return melhor, max

peganota(2,1,5,3,3,'A','B','C','D','E')



