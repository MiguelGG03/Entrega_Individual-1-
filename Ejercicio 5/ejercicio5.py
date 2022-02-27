class persona:
  
    def __init__(self,cliente,identidad,direccion):
        self.cliente=cliente
        self.identidad=identidad
        self.direccion=direccion

    def vive_en(self,ciu):
        if(ciu==self.direccion):
            return True
        else:
            return False

    def es_cliente(self):
        if(self.cliente==1):
            return True
        else:
            return False

personas=[]
# inicializo personas
personas.append(persona(0,'Juan','TOLEDO'))
personas.append(persona(1,'Luis','TOLEDO'))
personas.append(persona(0,'Miguel','SEVILLA'))
personas.append(persona(1,'David','MADRID'))

don=str(input('Donde vive el cliente:'))
donde=don.upper()

print()

for i in (personas):
    if(i.es_cliente()==False):
        print("La persona "+i.identidad+ ' NO es cliente')
    else:
        if(i.vive_en(donde)==True):
            print("La persona "+i.identidad+ ' es cliente de '+donde)
        else:
            print("La persona "+i.identidad+ ' NO es cliente de '+donde)

print()