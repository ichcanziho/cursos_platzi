class Clients:
    def __init__(self, name, client_id, credit, address):
        self.name = name
        self.client_id = client_id
        self.credit = credit
        self.address = address


def mostrar_cliente(cliente):
    print("*"*32)
    print("Nombre: ", cliente.name)
    print("Id: ", cliente.client_id)
    print("Crédito: ", cliente.credit)
    print("Dirección: ", cliente.address)
    print("*" * 32)


if __name__ == '__main__':
    usuario_a = Clients("Gabriel", "0000004", "1000000", "Xalapa, Veracruz")
    mostrar_cliente(cliente=usuario_a)
