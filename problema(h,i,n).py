a=int(input('numarul 1= '))
b=int(input('numarul 2= '))
def suma_f():
    print("Suma= ",a+b)
suma_f()

def produs_f():
    print("Produsul= ",a*b)
produs_f()

def nr_div(n):
    div=[]
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)
    return(len(div))

if nr_div(a)==nr_div(b):print("PRIETENE")