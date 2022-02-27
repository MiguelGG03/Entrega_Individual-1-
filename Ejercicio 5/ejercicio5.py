class persona:
  #  cliente=0
   # identidad=''
    #direccion=''    
    def __init__(self,cliente,identidad,direccion):
        self.cliente=cliente
        self.identidad=identidad
        self.direccion=direccion

    @classmethod
    def vive_en(self,ciu):
        print('Es de '+ciu+' - '+self.direccion)        
        if(ciu==self.direccion):
            return True
        else:
            return False

    def es_cliente(self,cli):
        if(cli==1):
            print('Es cliente')
        else:
            print('No es cliente')

personas=[]
# inicializo personas
personas.append(persona(0,'Juan','TOLEDO'))
personas.append(persona(1,'Luis','TOLEDO'))
personas.append(persona(0,'Miguel','SEVILLA'))
personas.append(persona(1,'David','MADRID'))

donde=str(input('Donde vive el cliente:'))

for i in (personas):
    print(i.direccion)
    if(i.vive_en(donde)==True):
        print(i.identidad+ ' es de '+donde)
    else:
        print(i.identidad+ ' NO es de '+donde)