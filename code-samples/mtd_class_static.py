class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_pessoa_com_data_nascimento(cls, nome, ano, mes, dia):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def validar_maior_idade(idade):
        return idade >= 18
    
pessoa = Pessoa("maria", 2000)
print(pessoa.nome, pessoa.idade)

# Utilizamos o None nos argumentos da função de inicialização pois ao chamar
# Pessoa(), na linha abaixo não passamos nenhum arugmento e iremos tornar essa
# atribuição dinâmica na função criar_pessoa_com_data_nascimento()
#     def criar_pessoa_com_data_nascimento(self, nome, ano, mes, dia):
#       idade = 2024 - ano
#       return Pessoa(nome, idade)
# pessoa1 = Pessoa().criar_pessoa_com_data_nascimento("maru", 2000, 3, 21)

# Temos um problema na chamadas acima, Pessoa() cria uma instância de Pessoa e o
# método criar_pessoa_com_data_nascimento("maru", 2000, 3, 21) cria outra instância
# assim criando duas instâncias desnecessariamente

# Para resolver este problema utilza-se o método de classe @classmethod
# criando da maneira correta
pessoa2 = Pessoa.criar_pessoa_com_data_nascimento("tutu", 2000, 3, 21)
print(pessoa2.nome, pessoa2.idade)

print(Pessoa.validar_maior_idade(pessoa2.idade))
print(Pessoa.validar_maior_idade(9))