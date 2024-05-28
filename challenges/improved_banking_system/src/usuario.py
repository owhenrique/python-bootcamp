class Usuario:
    def __init__(self, nome, data_nascimento, CPF, **kwargs):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = CPF
        self.endereco = "\n".join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])

    def getCpf(self):
        return self.cpf
    
    def getEndereco(self):
        return self.endereco

    def __repr__(self):
        return __str__(self)

    def __str__(self):
        return f"cliente: {self.nome}, {self.data_nascimento}, {self.cpf}, {self.endereco}"


# paulo = Usuario('Paulo', '24/11/1999', '02401032118', logradouro=42, numero=52, bairro='gama', cidade='df', estado='distrito federal')
# print(paulo.getCpf())
# print(paulo.getEndereco())