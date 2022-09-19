a=int(input('numarul 1= '))
b=int(input('numarul 2= '))
divizori=[]
def mult_minim(a, b):return (a * b) // divizori[-1]

print("Cel mai mic multiplu comun= ",mult_minim(a, b))

multipli=[]
def com_mult_5(a,b):
    x=a*b
    for i in range(5):
        multipli.append(x)
        x=x*2
com_mult_5(a,b)

print("Cinci multipli comuni:",*multipli,sep=' ')