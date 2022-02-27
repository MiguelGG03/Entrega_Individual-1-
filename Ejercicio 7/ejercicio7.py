col=str(input('Introduzca los colores (R),(V),(Otros),(A): '))
color=col.upper()

r=0
v=0
a=len(color)-1

colores=[]
for j in range(0,a+1):
    colores.append(color[j:j+1])

while(v<=a):
    if(colores[v]=='V'):
        v=v+1
    else:
        if(colores[v]=='R'):
            aux=colores[v]
            colores[v]=colores[r]
            colores[r]=aux
            r=r+1
            v=v+1
        else:
            colores[v]='A'
            aux=colores[v]
            colores[v]=colores[a]
            colores[a]=aux
            a=a-1


print(colores)