a=int(input('numarul 1= '))
b=int(input('numarul 2= '))
divizori=[]
def cmdc(a, b):
    n=0
    for i in range(1, min(a, b)+1):
        if a%i==b%i==0:
            n+=1
            divizori.append(i)
cmdc(a, b)

print("Cel mai mare divizor comun= ",divizori[-1])

print("Toti divizorii comuni:",*divizori,sep=' ')