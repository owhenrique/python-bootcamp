class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={value}" for chave, value in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(numero_patas=kwargs["numero_patas"])
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorinco(Mamifero, Ave):
    pass


gato = Gato(numero_patas=4, cor_pelo="preto")
print(gato)

ornitorinco = Ornitorinco(numero_patas=4, cor_pelo="fulvo", cor_bico="marrom")
print(ornitorinco)
