def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("ERRO: Este cliente não possui contas!")
        return
    
    return cliente.contas[0]