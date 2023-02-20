class Asiento:
    def _init_(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        colores=['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if color in colores:
            self.color=color

class Auto:
    cantidadCreados=0
    def _init_(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=[]
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        total=0
        for i in self.asientos:
            if len[i]!=0:#isinstance(i,Asiento) ó if i in Asiento
                total+=1
        return total
    
    def verificarIntegridad(self):
        result=True
        if self.registro==Motor.registro:
            for i in Asiento.asiento:
                if i.registro!=self.registro:
                    result=False
                    break 

        if result==True:
            return 'Auto original'
        else:
            return 'Las piezas no son originales'



class Motor:
    def _init_(self,numero,tipo,registro):
        self.numero=numero
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if tipo=='gasolina'or'electrico':
            self.tipo=tipo

            

