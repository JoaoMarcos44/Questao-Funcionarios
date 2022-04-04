maior = 0
l=[]
f= 0
s= 0

for c in range(1,11):
    print("{}funcionários".format(c))
    h= float(input("horas trabalhadas:"))
    v= float(input("valor/hora: "))
    if h<160:
        s=h*v
    if h> 160:
        he=(h-160)*(1.5*v)
        s= v*160+he
    l+=[s]
    if h>maior:
        maior= h
        f=c
for p in range(0,10):
    print("funcionários{}".format(p+1))
    print("salário:{:.2f}R$".format(l[p]))
print("Parabéns funcionário {} por trabalhar mais horas ({} horas/mês)".format(f,maior))
