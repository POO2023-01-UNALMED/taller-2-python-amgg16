class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        colores=['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if color in colores:
            self.color=color

class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        total=0
        for i in self.asientos:
            if i!=None:#isinstance(i,Asiento) ó if i in Asiento
                total+=1
        return total
    
    def verificarIntegridad(self):
        result=True
        for i in self.asiento:
            if i!=None:
                if i.registro!=self.registro:
                    result=False 
                    break
        if self.registro!=self.motor.registro:
            result=False

        if result==True:
            return 'Auto original'
        else:
            return 'Las piezas no son originales'



class Motor:
    def __init__(self,numero,tipo,registro):
        self.numero=numero
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if tipo=='gasolina'or tipo=='electrico':
            self.tipo=tipo

            

