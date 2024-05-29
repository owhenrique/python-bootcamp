def filtrar_cliente(clientes) -> object or None:
    cpf = input("Informe o cpf do cliente: ")
    clientes = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes[0] if clientes else None