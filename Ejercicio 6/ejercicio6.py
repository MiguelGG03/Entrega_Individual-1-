frase=str(input('Introduzca la frase: '))

cont=0
max=0

letras=[]
h=int(len(frase))

for j in range(0,h):
    if(frase[j:j+1]!=' '):
        letras.append(frase[j:j+1])
        max=max+1

#max es la longitud de la frase sin blancos

while(letras[cont]==letras[max-1-cont] and cont<max/2):
    print(str(cont)+letras[cont]+letras[max-1-cont])
    cont=cont+1

if(cont==int(max/2)):
    print('Es palindromo '+frase)
else:
    print('No es palidromo '+frase)
    