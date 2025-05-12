import csv
import config

class Cliente:
    def __init__(self, dni, nombre , apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellido}"


class Clientes:
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente