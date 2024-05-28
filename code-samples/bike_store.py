class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha=1):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha

    def buzinar(self):
        print("plim plim...")

    def parar(self):
        print("freiando...")
        print("bicicleta parada!")

    def correr(self):
        print("pedalando...")
        print("bicicleta correndo!")
    
    # def get_cor(self):
    #     return self.cor

    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

caloi = Bicicleta("vermelha", "caloi", 2024, 1600)

print(vars(caloi))
print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)

caloi.buzinar()        # É equivalente a isto Bicicleta.buzinar(caloi)
caloi.correr()
caloi.parar()
# print(caloi.get_cor())
print(caloi.__str__())