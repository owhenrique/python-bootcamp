class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={value}" for chave, value in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado=False):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{"sim, " if self.carregado else "nao"} estou carregado")

    def carregar_caminhao(self, carregado=True):
        self.carregado = carregado


moto = Motocicleta("vermelhor", "abc-123", 2)
moto.ligar_motor()
print(moto.__str__())

carro = Carro("branco", "abc-234", 4)
carro.ligar_motor()
print(carro.__str__())

caminhao = Caminhao("azul", "abc-345", 8)
caminhao.ligar_motor()
caminhao.esta_carregado()
caminhao.carregar_caminhao()
caminhao.esta_carregado()
print(caminhao.__str__())