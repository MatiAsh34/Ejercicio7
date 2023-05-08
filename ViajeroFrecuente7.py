import csv

class ViajeroFrecuente:
    def __init__(self,num,dni,nom,apellido,millas):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apellido
        self.__millas_acum = millas

    def __gt__ (self,otroViajero):
        if self.__millas_acum > otroViajero.getTotalMillas():
            return self.__millas_acum

    def __add__(self,millas):
        return self.__millas_acum + millas

    def __sub__(self,millas):
        return self.__millas_acum - millas

    def __eq__(self,millas):
        return self.__millas_acum == millas

    def getNumViajero(self):
        return self.__num_viajero

    def getTotalMillas(self):
        return (int(self.__millas_acum))
    
class manejadorViajero:
    def __init__(self):
        self.__listaViajero= []

    def agregarViajero(self):
        archivo = open('DatosViajeros7.csv')
        reader = csv.reader(archivo,delimiter=',')

        for fila in reader:
            unViajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],int(fila[4]))
            self.__listaViajero.append(unViajero)

        archivo.close()

    def buscaViajero(self,num):
        i=0
        Retorno = None
        b = False

        while not b and i < len(self.__listaViajero):
            if self.__listaViajero[i].getNumViajero()==num:
                b =True
                Retorno=i
            else:
                i+=1
        return Retorno

    def getMillas(self,n):
        return self.__listaViajero[n].getTotalMillas()

    def acumularMillas(self,nuevas_millas,n):
        return self.__listaViajero[n] + nuevas_millas

    def canjearMillas(self,cant,n):
        return self.__listaViajero[n] - cant

    def compararMillas(self,cant,n):
        if self.__listaViajero[n] == cant:
            print("Las millas ingresadas son iguales.")

        else:
            print("Las millas ingresadas no son iguales.")

    def comparaViajeros(self):
        maximo = max(self.__listaViajero)
        for i in range(len(self.__listaViajero)):
            if self.__listaViajero[i].getTotalMillas() == maximo.getTotalMillas():
                print("El viajero",self.__listaViajero[i].getNumViajero(),"tiene el maximo de millas.")