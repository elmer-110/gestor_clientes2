class Cliente:
    def __init__(self, dni, nombre , apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellido}"


class Clientes:
    lista=[]
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
        return None
    def crear_cliente(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente
    def modificar_cliente(dni, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                return Clientes.lista[i]
    def eliminar_cliente(dni):
        for i, cliente in enumerate(Clientes.lista):
            if  cliente.dni == dni:
                cliente = Clientes.lista.pop(i)
                return cliente      
            